"""Structural tests of the AT3 Ledgerline lab-pack templates - run with NO AWS account.

Asserts the invariants that make this a valid existing-state baseline + a valid improvement
change-set, honouring the AWS Academy constraints and - critically - that the improvement actually
moves BOTH tiers to Multi-AZ: the baseline is single-AZ, the improved template is not.

Templates are parsed with cfn-lint's decoder so the intrinsic tags (!Ref, !GetAtt, !Sub, !Select,
!If, !GetAZs) load correctly.

Run from the lab-pack folder:  python -m pytest
"""
from pathlib import Path

from cfnlint.decode import cfn_yaml

LAB = Path(__file__).resolve().parent.parent
BASELINE = LAB / "baseline.yaml"
IMPROVED = LAB / "improved.yaml"
ALL_TEMPLATES = [BASELINE, IMPROVED]


def _load(path):
    loaded = cfn_yaml.load(str(path))
    return loaded[0] if isinstance(loaded, tuple) else loaded


def _of_type(template, resource_type):
    return {k: v for k, v in template["Resources"].items() if v.get("Type") == resource_type}


# ---- decode / structure ----

def test_all_templates_decode():
    for path in ALL_TEMPLATES:
        t = _load(path)
        assert "Resources" in t and t["Resources"], f"{path.name} has no resources"


# ---- the central invariant: the improvement converts the database to Multi-AZ ----

def test_baseline_rds_is_single_az():
    # The baseline is the existing state the student improves FROM - a single instance, no standby.
    for name, db in _of_type(_load(BASELINE), "AWS::RDS::DBInstance").items():
        assert db["Properties"].get("MultiAZ") is False, \
            f"baseline:{name} must be single-AZ - it is the starting state"


def test_improved_rds_is_multi_az():
    # The improvement converts it in place. MultiAZ is an update property, so the instance is
    # modified, not replaced, and the data survives.
    dbs = _of_type(_load(IMPROVED), "AWS::RDS::DBInstance")
    assert dbs, "improved.yaml has no RDS instance"
    for name, db in dbs.items():
        assert db["Properties"].get("MultiAZ") is True, \
            f"improved:{name} must be Multi-AZ - that is the database-tier improvement"


def test_rds_engine_matches_across_templates():
    # Engine is a REPLACEMENT property: if the two templates disagree, the change-set destroys and
    # rebuilds the database instead of updating it. Both must be PostgreSQL, per the scenario.
    defaults = set()
    for path in (BASELINE, IMPROVED):
        t = _load(path)
        assert _of_type(t, "AWS::RDS::DBInstance"), f"{path.name} has no RDS instance"
        default = t["Parameters"]["DBEngine"]["Default"]
        assert default == "postgres", f"{path.name} DBEngine default must be postgres, got {default}"
        defaults.add(default)
    assert len(defaults) == 1, f"templates disagree on DBEngine: {defaults}"


def test_rds_encrypted_and_empty():
    # Encrypted at rest, and no DBName - the instance comes up with no user database.
    for path in (BASELINE, IMPROVED):
        for name, db in _of_type(_load(path), "AWS::RDS::DBInstance").items():
            assert db["Properties"].get("StorageEncrypted") is True, f"{path.name}:{name} must be encrypted"
            assert "DBName" not in db["Properties"], f"{path.name}:{name} must have no DBName (empty)"


# ---- compute: single-AZ baseline -> 2-AZ improved ----

def test_baseline_compute_is_single_az():
    asgs = _of_type(_load(BASELINE), "AWS::AutoScaling::AutoScalingGroup")
    assert asgs, "baseline has no Auto Scaling group"
    for name, asg in asgs.items():
        zones = asg["Properties"]["VPCZoneIdentifier"]
        assert len(zones) == 1, f"baseline {name} must span ONE subnet (the improvement spreads it)"


def test_improved_compute_is_multi_az():
    asgs = _of_type(_load(IMPROVED), "AWS::AutoScaling::AutoScalingGroup")
    assert asgs, "improved has no Auto Scaling group"
    for name, asg in asgs.items():
        zones = asg["Properties"]["VPCZoneIdentifier"]
        assert len(zones) == 2, f"improved {name} must span TWO subnets (application-tier Multi-AZ)"


def test_improved_changes_only_multi_az_on_the_db():
    # The change-set is applied to the SAME stack, so the Database must be MODIFIED in place, never
    # replaced. The only property the improvement may change is MultiAZ (an in-place update property).
    # Anything else differing - especially Engine, DBInstanceIdentifier or MasterUsername - would
    # trigger a replacement and destroy the financial data.
    base_db = next(iter(_of_type(_load(BASELINE), "AWS::RDS::DBInstance").values()))
    imp_db = next(iter(_of_type(_load(IMPROVED), "AWS::RDS::DBInstance").values()))
    differing = {k for k in set(base_db["Properties"]) | set(imp_db["Properties"])
                 if base_db["Properties"].get(k) != imp_db["Properties"].get(k)}
    assert differing == {"MultiAZ"}, \
        f"improved.yaml may only change MultiAZ on the Database; also differs: {sorted(differing - {'MultiAZ'})}"
    assert base_db["Properties"]["MultiAZ"] is False and imp_db["Properties"]["MultiAZ"] is True, \
        "the improvement must take the database from single-AZ to Multi-AZ"

def test_alb_is_internal():
    for path in (BASELINE, IMPROVED):
        albs = _of_type(_load(path), "AWS::ElasticLoadBalancingV2::LoadBalancer")
        assert albs, f"{path.name} has no load balancer"
        for name, alb in albs.items():
            assert alb["Properties"]["Scheme"] == "internal", f"{path.name}:{name} must be an internal ALB"


# ---- AWS Academy constraints ----

def test_no_iam_resources_created():
    iam = {"AWS::IAM::Role", "AWS::IAM::User", "AWS::IAM::Group", "AWS::IAM::Policy",
           "AWS::IAM::ManagedPolicy", "AWS::IAM::InstanceProfile"}
    for path in ALL_TEMPLATES:
        found = [k for k, v in _load(path)["Resources"].items() if v.get("Type") in iam]
        assert not found, f"{path.name}: Academy forbids creating IAM; found {found}"


def test_instance_profile_defaults_to_the_lab_profile():
    # Session Manager is how the baseline is administered (no key pair, no inbound management port),
    # and that needs the lab's own profile attached. The pack still creates no IAM of its own.
    for path in (BASELINE, IMPROVED):
        t = _load(path)
        assert t["Parameters"]["InstanceProfileName"].get("Default") == "LabInstanceProfile", \
            f"{path.name}: instance profile must default to LabInstanceProfile"
        assert "HasInstanceProfile" in t.get("Conditions", {}), f"{path.name}: expected HasInstanceProfile"


def test_ami_resolved_via_ssm_parameter():
    for path in (BASELINE, IMPROVED):
        ami = _load(path)["Parameters"]["AmiId"]
        assert ami["Type"] == "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>", \
            f"{path.name}: AMI must come from an SSM public parameter"


def test_buckets_block_public_access():
    for path in ALL_TEMPLATES:
        buckets = _of_type(_load(path), "AWS::S3::Bucket")
        assert buckets, f"{path.name} has no S3 buckets"
        for name, bucket in buckets.items():
            pab = bucket["Properties"]["PublicAccessBlockConfiguration"]
            for flag in ("BlockPublicAcls", "BlockPublicPolicy", "IgnorePublicAcls", "RestrictPublicBuckets"):
                assert pab[flag] is True, f"{path.name}:{name}.{flag} must be true"


# ---- pure ASCII (a non-ASCII char in an RDS description fails the live deploy; cfn-lint misses it) ----

def test_templates_are_pure_ascii():
    for path in ALL_TEMPLATES:
        raw = path.read_bytes()
        try:
            raw.decode("ascii")
        except UnicodeDecodeError as exc:
            raise AssertionError(f"{path.name} contains a non-ASCII byte at offset {exc.start}") from exc
