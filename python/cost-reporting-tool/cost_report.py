#!/usr/bin/env python3
"""
Tilington plc — AWS Cost Reporting Tool
Cloud Modernisation Programme

STATUS: STARTER — Candidate completes in Phase 4

This script generates monthly cost reports by service, account, and tag.
Currently only total cost retrieval is implemented.
Candidate must add: per-service breakdown, per-tag breakdown, savings recommendations.

Usage:
    python3 cost_report.py --start 2026-01-01 --end 2026-01-31
    python3 cost_report.py --month 2026-03 --output cost-report.csv

Requirements:
    pip install boto3 pandas
    AWS CLI configured with Cost Explorer access (management account)

Note: Cost Explorer API must be enabled in the management account.
      There is a $0.01 per API request charge — batch requests efficiently.
"""

import boto3
import csv
import json
import argparse
import logging
from datetime import datetime, date
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Tilington programme budget
MONTHLY_BUDGET = 56_667  # £3.2M / 18 months = ~£56,667/month
CURRENCY = "USD"  # Cost Explorer returns USD — candidate converts to GBP


def get_total_monthly_cost(ce_client, start_date: str, end_date: str) -> dict:
    """
    Get total AWS spend for a given date range.
    
    Args:
        ce_client: Boto3 Cost Explorer client
        start_date: Start date in YYYY-MM-DD format (inclusive)
        end_date: End date in YYYY-MM-DD format (exclusive)
        
    Returns:
        Dictionary with total cost and currency
    """
    response = ce_client.get_cost_and_usage(
        TimePeriod={"Start": start_date, "End": end_date},
        Granularity="MONTHLY",
        Metrics=["BlendedCost"]
    )
    
    total = float(response["ResultsByTime"][0]["Total"]["BlendedCost"]["Amount"])
    unit = response["ResultsByTime"][0]["Total"]["BlendedCost"]["Unit"]
    
    return {"amount": total, "unit": unit}


def get_cost_by_service(ce_client, start_date: str, end_date: str) -> list[dict]:
    """
    TODO: Implement cost breakdown by AWS service.
    
    Use GroupBy SERVICE to get per-service costs.
    Expected output should include at minimum:
    - Amazon EC2
    - Amazon RDS
    - Amazon EKS
    - Amazon S3
    - AWS Data Transfer
    - AWS KMS
    - Amazon CloudWatch
    - Amazon Route 53
    
    Sort by cost descending. Flag any service exceeding 30% of total spend.
    
    Returns:
        List of dicts: [{service, amount, unit, percentage_of_total}]
    """
    # TODO: Implement this function
    # Hint: Use GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}]
    logger.warning("get_cost_by_service not yet implemented")
    return []


def get_cost_by_tag(ce_client, start_date: str, end_date: str, tag_key: str = "Application") -> list[dict]:
    """
    TODO: Implement cost breakdown by resource tag.
    
    Required tag keys to report on:
    - Application (which app is driving cost)
    - Environment (prod vs non-prod split)
    - CostCentre (chargeback to business units)
    
    Note: Tags must be activated in Cost Allocation Tags in the management account.
    Flag any untagged spend (tag value = "") as a governance issue.
    
    Returns:
        List of dicts: [{tag_value, amount, unit, percentage_of_total}]
    """
    # TODO: Implement this function
    # Hint: Use GroupBy=[{"Type": "TAG", "Key": tag_key}]
    logger.warning(f"get_cost_by_tag not yet implemented for tag: {tag_key}")
    return []


def get_savings_recommendations(ce_client) -> dict:
    """
    TODO: Implement Savings Plans and Reserved Instance recommendations.
    
    Use Cost Explorer recommendations APIs:
    - ce_client.get_savings_plans_purchase_recommendation()
    - ce_client.get_reservation_purchase_recommendation()
    
    Expected output:
    - Estimated monthly savings from Savings Plans
    - Coverage % currently covered by commitments
    - Recommended commitment amount
    - Payback period
    
    Tilington context: EC2 and EKS node groups are candidates for Compute Savings Plans.
    Aurora PostgreSQL is a candidate for RDS Reserved Instances.
    
    Returns:
        Dictionary with savings recommendations and estimated annual saving
    """
    # TODO: Implement this function
    logger.warning("get_savings_recommendations not yet implemented")
    return {"estimated_monthly_saving": 0, "recommended_action": "TODO: Implement"}


def generate_budget_vs_actual_report(actual_monthly: float, budget_monthly: float = MONTHLY_BUDGET) -> dict:
    """
    TODO: Generate a budget vs actual comparison.
    
    Calculate:
    - Variance (actual - budget)
    - Variance % ((actual - budget) / budget * 100)
    - Status: UNDER_BUDGET, ON_TRACK (within 10%), OVER_BUDGET
    - Projected annual spend at current rate
    - Projected annual variance vs programme budget
    
    Note: Cost Explorer returns USD. Apply current GBP/USD rate.
    Hardcode rate for now; production would use an FX API.
    
    Returns:
        Dictionary with budget analysis
    """
    # TODO: Implement this function
    # Current approximate GBP/USD rate (update this):
    GBP_USD_RATE = 1.27
    
    actual_gbp = actual_monthly / GBP_USD_RATE
    variance = actual_gbp - budget_monthly
    variance_pct = (variance / budget_monthly) * 100
    
    return {
        "actual_usd": actual_monthly,
        "actual_gbp": round(actual_gbp, 2),
        "budget_gbp": budget_monthly,
        "variance_gbp": round(variance, 2),
        "variance_pct": round(variance_pct, 1),
        "status": "TODO: Implement status logic",
        "projected_annual_gbp": round(actual_gbp * 12, 2),
        # TODO: Add comparison to £3.2M programme budget
    }


def main():
    parser = argparse.ArgumentParser(description="Tilington AWS Cost Reporting Tool")
    parser.add_argument("--start", help="Start date YYYY-MM-DD")
    parser.add_argument("--end", help="End date YYYY-MM-DD")
    parser.add_argument("--month", help="Month shorthand: 2026-03")
    parser.add_argument("--profile", default="default", help="AWS CLI profile (management account)")
    parser.add_argument("--output", default="cost-report.csv", help="Output filename")
    args = parser.parse_args()
    
    # Resolve date range
    if args.month:
        year, month = map(int, args.month.split("-"))
        import calendar
        _, last_day = calendar.monthrange(year, month)
        start_date = f"{year}-{month:02d}-01"
        end_date = f"{year}-{month:02d}-{last_day}"
    elif args.start and args.end:
        start_date = args.start
        end_date = args.end
    else:
        # Default: current month to date
        today = date.today()
        start_date = today.replace(day=1).isoformat()
        end_date = today.isoformat()
    
    logger.info(f"Cost report: {start_date} to {end_date}")
    
    session = boto3.Session(profile_name=args.profile)
    ce = session.client("ce", region_name="us-east-1")  # Cost Explorer is global, always us-east-1
    
    # Get total cost (implemented)
    total = get_total_monthly_cost(ce, start_date, end_date)
    logger.info(f"Total cost: {total['amount']:.2f} {total['unit']}")
    
    # Budget vs actual (partial)
    budget_report = generate_budget_vs_actual_report(total["amount"])
    
    print(f"\n=== Tilington AWS Cost Report ===")
    print(f"Period: {start_date} to {end_date}")
    print(f"Total spend: ${total['amount']:.2f} USD / £{budget_report['actual_gbp']:.2f} GBP")
    print(f"Monthly budget: £{budget_report['budget_gbp']:,.0f} GBP")
    print(f"Variance: £{budget_report['variance_gbp']:,.0f} GBP ({budget_report['variance_pct']}%)")
    print(f"\nTODO: Implement get_cost_by_service, get_cost_by_tag, get_savings_recommendations")
    print(f"TODO: Export full report to {args.output}")


if __name__ == "__main__":
    main()
