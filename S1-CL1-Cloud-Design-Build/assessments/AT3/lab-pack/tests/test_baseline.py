"""Structural test of the AT3 baseline template — runs with NO AWS account.

Asserts two things. First, the invariants that make this a valid *non-HA baseline* (the thing
AT3 hardens) and that honour the AWS Academy constraints. Second, that the template is still an
exact replica of AT2's end state — the names and settings a student who completed the AT2 build
run sheet correctly would have. If AT2's run sheet changes, this fails until the template
follows it.

Parses the template with cfn-lint's decoder so the CloudFormation intrinsic tags (!Ref, !GetAtt,
!Sub, !Select) load correctly.

Run from the lab-pack folder:  python -m pytest
"""
from pathlib import Path

from cfnlint.decode import cfn_yaml

TEMPLATE = Path(__file__).resolve().parent.parent / "baseline.yaml"


def _load():
    loaded = cfn_yaml.load(str(TEMPLATE))
    template = loaded[0] if isinstance(loaded, tuple) else loaded
    return template


def _of_type(template, resource_type):
    return {k: v for k, v in template["Resources"].items() if v.get("Type") == resource_type}


def _named(template, resource_type, name_property):
    """The values of `name_property` across every resource of `resource_type`."""
    return {v["Properties"][name_property] for v in _of_type(template, resource_type).values()}


def _tag_names(template, resource_type):
    """The Name tag of every resource of `resource_type`."""
    out = set()
    for res in _of_type(template, resource_type).values():
        for tag in res["Properties"].get("Tags", []):
            if tag.get("Key") == "Name":
                out.add(tag["Value"])
    return out


def test_template_decodes():
    t = _load()
    assert "Resources" in t and t["Resources"]


# ---------------------------------------------------------------- non-HA invariants

def test_rds_is_single_az():
    # The baseline DB is Single-AZ; enabling Multi-AZ is the AT3 hardening step.
    for name, db in _of_type(_load(), "AWS::RDS::DBInstance").items():
        assert db["Properties"].get("MultiAZ") is False, f"{name} must be Single-AZ in the baseline"


def test_compute_is_single_az():
    # The ASG runs in ONE subnet/AZ; spreading it across AZs is the AT3 hardening step.
    asgs = _of_type(_load(), "AWS::AutoScaling::AutoScalingGroup")
    assert asgs, "no Auto Scaling group"
    for name, asg in asgs.items():
        zones = asg["Properties"]["VPCZoneIdentifier"]
        assert len(zones) == 1, f"{name} must span ONE subnet in the baseline (AT3 spreads it)"


# ---------------------------------------------------------------- Academy constraints

def test_no_iam_resources_created():
    # AWS Academy Learner Lab forbids creating IAM. AT2 tasks 8 and 9 reflect that: task 8 is a
    # deliberate refusal, task 9 reviews the supplied LabRole. Neither builds anything.
    iam = {"AWS::IAM::Role", "AWS::IAM::User", "AWS::IAM::Group", "AWS::IAM::Policy",
           "AWS::IAM::ManagedPolicy", "AWS::IAM::InstanceProfile"}
    found = [k for k, v in _load()["Resources"].items() if v.get("Type") in iam]
    assert not found, f"Academy forbids creating IAM resources; found {found}"


def test_instance_profile_defaults_to_the_lab_profile():
    # AT2 task 10 selects LabInstanceProfile, and the app instances are private with no public
    # IP, so it is also the only route to a shell on them. Blank stays available as an escape.
    t = _load()
    assert t["Parameters"]["InstanceProfileName"].get("Default") == "LabInstanceProfile"
    assert "HasInstanceProfile" in t.get("Conditions", {}), "expected the HasInstanceProfile condition"


def test_ami_resolved_via_ssm_parameter():
    # No hardcoded AMI to go stale — resolved from an SSM public parameter, which is what AT2
    # task 10's "latest Windows Server available" resolves to.
    ami = _load()["Parameters"]["WindowsAmiId"]
    assert ami["Type"] == "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>"


# ---------------------------------------------------------------- AT2 replica fidelity

def test_five_subnets_with_at2_names_and_cidrs():
    subnets = _of_type(_load(), "AWS::EC2::Subnet")
    assert len(subnets) == 5, "AT2 task 3 builds exactly five subnets"
    cidrs = {v["Properties"]["CidrBlock"] for v in subnets.values()}
    assert cidrs == {"10.0.1.0/24", "10.0.2.0/24", "10.0.11.0/24", "10.0.21.0/24", "10.0.22.0/24"}
    assert _tag_names(_load(), "AWS::EC2::Subnet") == {
        "public-web-a", "public-web-b", "private-app-a", "private-data-a", "private-data-b"}


def test_data_subnets_stay_on_the_default_route_table():
    # AT2 task 6 builds two route tables and deliberately leaves the data subnets on the VPC
    # default, which carries no internet route. So no association may name a data subnet.
    t = _load()
    tables = _of_type(t, "AWS::EC2::RouteTable")
    assert len(tables) == 2, "AT2 task 6 builds two route tables, not three"
    assoc_subnets = {str(v["Properties"]["SubnetId"])
                     for v in _of_type(t, "AWS::EC2::SubnetRouteTableAssociation").values()}
    assert not any("Data" in s for s in assoc_subnets), \
        "the data subnets must stay on the VPC default route table"


def test_security_groups_match_at2_names_and_rules():
    t = _load()
    assert _named(t, "AWS::EC2::SecurityGroup", "GroupName") == {
        "yat-lms-alb-sg", "yat-lms-app-sg", "yat-lms-db-sg"}
    # AT2 builds no RDP rule — the app tier is private and reached via Session Manager.
    for name, sg in _of_type(t, "AWS::EC2::SecurityGroup").items():
        for rule in sg["Properties"].get("SecurityGroupIngress", []):
            assert rule["FromPort"] != 3389, f"{name} has an RDP rule AT2 does not build"


def test_resource_names_match_the_at2_run_sheet():
    t = _load()
    assert _named(t, "AWS::EC2::LaunchTemplate", "LaunchTemplateName") == {"yat-lms-lt"}
    assert _named(t, "AWS::ElasticLoadBalancingV2::TargetGroup", "Name") == {"yat-lms-tg"}
    assert _named(t, "AWS::ElasticLoadBalancingV2::LoadBalancer", "Name") == {"yat-lms-alb"}
    assert _named(t, "AWS::RDS::DBSubnetGroup", "DBSubnetGroupName") == {"yat-lms-db-subnet-group"}
    assert _named(t, "AWS::RDS::DBInstance", "DBInstanceIdentifier") == {"yat-lms-db"}
    assert _tag_names(t, "AWS::EC2::VPC") == {"yat-lms-vpc"}


def test_decision_options_are_the_two_at2_offers():
    params = _load()["Parameters"]
    assert params["InstanceType"]["AllowedValues"] == ["t3.micro", "t3.small"]
    assert params["DBInstanceClass"]["AllowedValues"] == ["db.t3.micro", "db.t3.small"]


def test_exactly_the_two_at2_alarms():
    # AT2 task 16 builds two alarms. The earlier five-alarm set is not what a student ends with.
    alarms = _named(_load(), "AWS::CloudWatch::Alarm", "AlarmName")
    assert alarms == {"yat-lms-unhealthy-hosts", "yat-lms-db-storage-low"}


def test_no_s3_buckets():
    # The S3 bucket task was cut from AT2 — no performance criterion required it — so a correctly
    # completed AT2 build has no buckets, and neither does its replica.
    assert not _of_type(_load(), "AWS::S3::Bucket"), "AT2 no longer builds S3 buckets"


def test_expected_outputs_present():
    outputs = _load()["Outputs"]
    for key in ("AlbDnsName", "RdsEndpoint", "VpcId"):
        assert key in outputs, f"missing output: {key}"
