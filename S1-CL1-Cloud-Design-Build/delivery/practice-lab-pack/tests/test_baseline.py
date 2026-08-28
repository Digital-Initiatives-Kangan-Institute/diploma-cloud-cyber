"""Structural test of the Ledgerline practice baseline — runs with NO AWS account.

Asserts that the template is still an exact replica of the AT2 PRACTICE build run sheet's end
state, and that it stays clearly DIFFERENT from the assessment: a different address range, a
different operating system, a different database engine, different names. If the practice run
sheet changes, this fails until the template follows it.

Run from the practice-lab-pack folder:  python -m pytest
"""
from pathlib import Path

from cfnlint.decode import cfn_yaml

TEMPLATE = Path(__file__).resolve().parent.parent / "baseline.yaml"


def _load():
    loaded = cfn_yaml.load(str(TEMPLATE))
    return loaded[0] if isinstance(loaded, tuple) else loaded


def _of_type(template, resource_type):
    return {k: v for k, v in template["Resources"].items() if v.get("Type") == resource_type}


def _named(template, resource_type, name_property):
    return {v["Properties"][name_property] for v in _of_type(template, resource_type).values()}


def _tag_names(template, resource_type):
    out = set()
    for res in _of_type(template, resource_type).values():
        for tag in res["Properties"].get("Tags", []):
            if tag.get("Key") == "Name":
                out.add(tag["Value"])
    return out


def test_template_decodes():
    t = _load()
    assert "Resources" in t and t["Resources"]


# ---------------------------------------------------------------- practice, not the assessment

def test_address_range_is_ledgerlines_not_the_assessments():
    # 10.20.x.x, not 10.0.x.x — a student cannot lift practice values into the assessment.
    t = _load()
    assert _of_type(t, "AWS::EC2::VPC")["Vpc"]["Properties"]["CidrBlock"] == "10.20.0.0/16"
    for name, subnet in _of_type(t, "AWS::EC2::Subnet").items():
        assert subnet["Properties"]["CidrBlock"].startswith("10.20."), f"{name} is not in 10.20/16"


def test_platform_differs_from_the_assessment():
    # Amazon Linux + PostgreSQL, against the assessment's Windows + MySQL.
    t = _load()
    assert "amazon-linux" in t["Parameters"]["AmazonLinuxAmiId"]["Default"]
    for name, db in _of_type(t, "AWS::RDS::DBInstance").items():
        assert db["Properties"]["Engine"] == "postgres", f"{name} must be PostgreSQL, not MySQL"


def test_every_name_is_ledgerline_prefixed():
    t = _load()
    names = (_tag_names(t, "AWS::EC2::VPC") | _tag_names(t, "AWS::EC2::Subnet")
             | _named(t, "AWS::EC2::SecurityGroup", "GroupName"))
    assert names, "no names found"
    for n in names:
        assert n.startswith("ledgerline-"), f"{n} is not a Ledgerline name"


def test_db_security_group_allows_postgres_not_mysql():
    for name, sg in _of_type(_load(), "AWS::EC2::SecurityGroup").items():
        for rule in sg["Properties"].get("SecurityGroupIngress", []):
            assert rule["FromPort"] != 3306, f"{name} allows MySQL; practice uses PostgreSQL"


# ---------------------------------------------------------------- practice run sheet fidelity

def test_five_subnets_with_practice_names_and_cidrs():
    subnets = _of_type(_load(), "AWS::EC2::Subnet")
    assert len(subnets) == 5, "practice task 3 builds exactly five subnets"
    assert {v["Properties"]["CidrBlock"] for v in subnets.values()} == {
        "10.20.1.0/24", "10.20.2.0/24", "10.20.11.0/24", "10.20.21.0/24", "10.20.22.0/24"}
    assert _tag_names(_load(), "AWS::EC2::Subnet") == {
        "ledgerline-public-a", "ledgerline-public-b", "ledgerline-app-a",
        "ledgerline-data-a", "ledgerline-data-b"}


def test_data_subnets_stay_on_the_default_route_table():
    t = _load()
    assert len(_of_type(t, "AWS::EC2::RouteTable")) == 2, "practice task 6 builds two route tables"
    assoc_subnets = {str(v["Properties"]["SubnetId"])
                     for v in _of_type(t, "AWS::EC2::SubnetRouteTableAssociation").values()}
    assert not any("Data" in s for s in assoc_subnets), \
        "the data subnets must stay on the VPC default route table"


def test_resource_names_match_the_practice_run_sheet():
    t = _load()
    assert _named(t, "AWS::EC2::LaunchTemplate", "LaunchTemplateName") == {"ledgerline-lt"}
    assert _named(t, "AWS::ElasticLoadBalancingV2::TargetGroup", "Name") == {"ledgerline-tg"}
    assert _named(t, "AWS::ElasticLoadBalancingV2::LoadBalancer", "Name") == {"ledgerline-alb"}
    assert _named(t, "AWS::RDS::DBSubnetGroup", "DBSubnetGroupName") == {"ledgerline-db-subnet-group"}
    assert _named(t, "AWS::RDS::DBInstance", "DBInstanceIdentifier") == {"ledgerline-db"}


def test_both_alarms():
    # AT2 practice task 16 builds two alarms, so a pack claiming to reproduce a completed
    # practice build has to carry both.
    assert _named(_load(), "AWS::CloudWatch::Alarm", "AlarmName") == {
        "ledgerline-unhealthy-hosts", "ledgerline-db-storage-low"}


def test_storage_alarm_threshold_differs_from_the_assessment():
    # The practice threshold is 20% of 20 GiB; the assessment's is 15%. Deliberate — a student
    # cannot carry the number across from one to the other.
    alarms = [r for r in _load()["Resources"].values()
              if r["Type"] == "AWS::CloudWatch::Alarm"
              and r["Properties"]["AlarmName"] == "ledgerline-db-storage-low"]
    assert alarms and alarms[0]["Properties"]["Threshold"] == 4294967296


def test_load_balancer_is_reachable_from_a_browser():
    # Deliberate: the practice environment is public so students can see the page they built.
    for name, alb in _of_type(_load(), "AWS::ElasticLoadBalancingV2::LoadBalancer").items():
        assert alb["Properties"]["Scheme"] == "internet-facing", \
            f"{name} must be reachable from a browser — that is the point of the practice"


# ---------------------------------------------------------------- Academy constraints

def test_no_iam_resources_created():
    iam = {"AWS::IAM::Role", "AWS::IAM::User", "AWS::IAM::Group", "AWS::IAM::Policy",
           "AWS::IAM::ManagedPolicy", "AWS::IAM::InstanceProfile"}
    found = [k for k, v in _load()["Resources"].items() if v.get("Type") in iam]
    assert not found, f"Academy forbids creating IAM resources; found {found}"


def test_compute_is_single_az():
    asgs = _of_type(_load(), "AWS::AutoScaling::AutoScalingGroup")
    assert asgs, "no Auto Scaling group"
    for name, asg in asgs.items():
        assert len(asg["Properties"]["VPCZoneIdentifier"]) == 1, \
            f"{name} must span ONE subnet, as the practice run sheet builds it"


def test_expected_outputs_present():
    outputs = _load()["Outputs"]
    for key in ("AlbDnsName", "RdsEndpoint", "VpcId"):
        assert key in outputs, f"missing output: {key}"
