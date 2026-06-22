#!/usr/bin/env python3
"""
Tilington plc — AWS Inventory Tool
Cloud Modernisation Programme

STATUS: STARTER — Candidate completes in Phase 4

This script generates a CSV inventory of AWS resources across all accounts.
Currently only EC2 instances are implemented.
Candidate must add: RDS, S3, EKS, Lambda, ELB, Security Groups, VPCs.

Usage:
    python3 inventory.py --profile tilington-production --region eu-west-2
    python3 inventory.py --all-accounts --output inventory-report.csv

Requirements:
    pip install boto3 pandas
    AWS CLI configured with appropriate profiles
"""

import boto3
import csv
import json
import argparse
import logging
from datetime import datetime, timezone
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


def get_ec2_inventory(session: boto3.Session, account_id: str, region: str) -> list[dict]:
    """
    Retrieve EC2 instance inventory from an AWS account.
    
    Args:
        session: Boto3 session with appropriate credentials
        account_id: AWS account ID for this session
        region: AWS region to query
        
    Returns:
        List of dictionaries containing instance details
    """
    ec2 = session.client("ec2", region_name=region)
    instances = []
    
    try:
        # Paginate through all instances
        paginator = ec2.get_paginator("describe_instances")
        
        for page in paginator.paginate():
            for reservation in page["Reservations"]:
                for instance in reservation["Instances"]:
                    # Extract tags as a flat dictionary
                    tags = {tag["Key"]: tag["Value"] for tag in instance.get("Tags", [])}
                    
                    instances.append({
                        "account_id": account_id,
                        "region": region,
                        "resource_type": "EC2Instance",
                        "resource_id": instance["InstanceId"],
                        "name": tags.get("Name", "UNTAGGED"),
                        "state": instance["State"]["Name"],
                        "instance_type": instance.get("InstanceType", "unknown"),
                        "platform": instance.get("Platform", "linux"),
                        "private_ip": instance.get("PrivateIpAddress", ""),
                        "public_ip": instance.get("PublicIpAddress", ""),
                        "vpc_id": instance.get("VpcId", ""),
                        "subnet_id": instance.get("SubnetId", ""),
                        "launch_time": str(instance.get("LaunchTime", "")),
                        "environment": tags.get("Environment", "UNTAGGED"),
                        "application": tags.get("Application", "UNTAGGED"),
                        "owner": tags.get("Owner", "UNTAGGED"),
                        "cost_centre": tags.get("CostCentre", "UNTAGGED"),
                        "patch_group": tags.get("PatchGroup", "UNTAGGED"),
                        "ebs_optimized": instance.get("EbsOptimized", False),
                        "monitoring": instance.get("Monitoring", {}).get("State", "disabled"),
                    })
                    
    except Exception as e:
        logger.error(f"Failed to query EC2 in account {account_id}, region {region}: {e}")
        
    return instances


# ============================================================
# TODO: Candidate implements these functions in Phase 4
# ============================================================

def get_rds_inventory(session: boto3.Session, account_id: str, region: str) -> list[dict]:
    """
    TODO: Implement RDS instance and cluster inventory.
    
    Must capture:
    - DB identifier, engine, engine version
    - Instance class, storage size
    - Multi-AZ status
    - Encryption status (KMS key ID)
    - Backup retention period
    - Parameter group
    - VPC and subnet group
    - Tags (Name, Environment, Application, Owner, CostCentre)
    
    Critical for Oracle migration: identify all Oracle DB instances
    (engine: oracle-ee or oracle-se2)
    
    Returns:
        List of dictionaries matching the standard inventory schema
    """
    # TODO: Implement this function
    logger.warning("get_rds_inventory not yet implemented")
    return []


def get_s3_inventory(session: boto3.Session, account_id: str) -> list[dict]:
    """
    TODO: Implement S3 bucket inventory.
    
    Must capture:
    - Bucket name, creation date, region
    - Versioning status
    - Encryption type (SSE-S3, SSE-KMS, or NONE — flag unencrypted!)
    - Public access block settings (flag any bucket without full block)
    - Bucket policy status
    - Tags
    
    FCA compliance: unencrypted buckets or public buckets must be flagged
    as HIGH severity findings.
    
    Returns:
        List of dictionaries matching the standard inventory schema
    """
    # TODO: Implement this function
    logger.warning("get_s3_inventory not yet implemented")
    return []


def get_eks_inventory(session: boto3.Session, account_id: str, region: str) -> list[dict]:
    """
    TODO: Implement EKS cluster inventory.
    
    Must capture:
    - Cluster name, version, status
    - Kubernetes version (flag if below minimum supported version)
    - Endpoint access (public vs private — flag public endpoint!)
    - Logging enabled (API, audit, authenticator, controller manager, scheduler)
    - Node groups: count, instance types, desired/min/max capacity
    - Tags
    
    Returns:
        List of dictionaries matching the standard inventory schema
    """
    # TODO: Implement this function
    logger.warning("get_eks_inventory not yet implemented")
    return []


def get_security_findings(session: boto3.Session, account_id: str, region: str) -> list[dict]:
    """
    TODO: Implement Security Hub findings export.
    
    Must capture HIGH and CRITICAL findings from Security Hub.
    Filter by:
    - Severity: HIGH, CRITICAL
    - Status: ACTIVE (not RESOLVED)
    - Standards: AWS Foundational Security Best Practices, CIS AWS Foundations
    
    Returns:
        List of findings dictionaries for the security findings report
    """
    # TODO: Implement this function
    logger.warning("get_security_findings not yet implemented")
    return []


def export_to_csv(data: list[dict], filename: str) -> None:
    """Export inventory data to CSV."""
    if not data:
        logger.warning(f"No data to export to {filename}")
        return
        
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        if data:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            
    logger.info(f"Exported {len(data)} records to {filename}")


def main():
    parser = argparse.ArgumentParser(description="Tilington AWS Inventory Tool")
    parser.add_argument("--profile", default="default", help="AWS CLI profile name")
    parser.add_argument("--region", default="eu-west-2", help="AWS region")
    parser.add_argument("--output", default=f"inventory-{datetime.now().strftime('%Y%m%d-%H%M%S')}.csv",
                       help="Output CSV filename")
    args = parser.parse_args()
    
    logger.info(f"Starting Tilington AWS inventory — profile: {args.profile}, region: {args.region}")
    
    # Create session
    session = boto3.Session(profile_name=args.profile, region_name=args.region)
    sts = session.client("sts")
    account_id = sts.get_caller_identity()["Account"]
    
    logger.info(f"Authenticated to account: {account_id}")
    
    # Collect inventory
    all_resources = []
    
    # EC2 (implemented)
    logger.info("Collecting EC2 inventory...")
    ec2_resources = get_ec2_inventory(session, account_id, args.region)
    all_resources.extend(ec2_resources)
    logger.info(f"Found {len(ec2_resources)} EC2 instances")
    
    # TODO: Candidate adds calls to other inventory functions:
    # all_resources.extend(get_rds_inventory(session, account_id, args.region))
    # all_resources.extend(get_s3_inventory(session, account_id))
    # all_resources.extend(get_eks_inventory(session, account_id, args.region))
    
    # Export results
    export_to_csv(all_resources, args.output)
    
    # Print summary
    resource_types = {}
    for r in all_resources:
        rt = r.get("resource_type", "unknown")
        resource_types[rt] = resource_types.get(rt, 0) + 1
    
    print(f"\n=== Tilington AWS Inventory Summary ===")
    print(f"Account: {account_id}")
    print(f"Region: {args.region}")
    print(f"Total resources: {len(all_resources)}")
    for rt, count in sorted(resource_types.items()):
        print(f"  {rt}: {count}")
    print(f"Output: {args.output}")
    print(f"\nTODO: Complete get_rds_inventory, get_s3_inventory, get_eks_inventory")


if __name__ == "__main__":
    main()
