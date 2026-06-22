# ============================================================
# Tilington plc — Terraform Networking Module
# AWS Cloud Modernisation Programme
# ============================================================
# STATUS: INCOMPLETE — Candidate completes in Phase 4
# ============================================================

terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  # TODO: Configure remote state backend
  # backend "s3" {
  #   bucket         = "tilington-terraform-state"
  #   key            = "networking/terraform.tfstate"
  #   region         = "eu-west-2"
  #   encrypt        = true
  #   dynamodb_table = "tilington-terraform-locks"
  # }
}

provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      Programme   = "TilingtonCloudModernisation"
      Environment = var.environment
      ManagedBy   = "Terraform"
      Owner       = "CloudPlatformTeam"
    }
  }
}

# ============================================================
# VPC — Production
# ============================================================

resource "aws_vpc" "production" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "tilington-${var.environment}-vpc"
  }
}

# ============================================================
# SUBNETS
# TODO: Candidate must complete the subnet design
# Requirements:
# - 3 private subnets (application tier) across 3 AZs
# - 3 private subnets (data tier) across 3 AZs
# - 3 public subnets (ALB/NAT only) across 3 AZs
# - Correct CIDR allocation from the VPC range
# ============================================================

resource "aws_subnet" "public" {
  count             = length(var.public_subnet_cidrs)
  vpc_id            = aws_vpc.production.id
  cidr_block        = var.public_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]

  map_public_ip_on_launch = false  # Never auto-assign public IPs

  tags = {
    Name = "tilington-${var.environment}-public-${count.index + 1}"
    Tier = "public"
    # TODO: Add EKS subnet discovery tags
    # "kubernetes.io/role/elb" = "1"
  }
}

# TODO: Add private application subnets
# resource "aws_subnet" "private_app" { ... }

# TODO: Add private data subnets
# resource "aws_subnet" "private_data" { ... }

# ============================================================
# INTERNET GATEWAY
# ============================================================

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.production.id
  tags = {
    Name = "tilington-${var.environment}-igw"
  }
}

# ============================================================
# NAT GATEWAY
# TODO: Candidate decides: one NAT GW per AZ (HA) or single (cost)?
# Document the trade-off in an ADR.
# ============================================================

resource "aws_eip" "nat" {
  count  = var.nat_gateway_count
  domain = "vpc"
  tags = {
    Name = "tilington-${var.environment}-nat-eip-${count.index + 1}"
  }
}

# resource "aws_nat_gateway" "main" {
#   count         = var.nat_gateway_count
#   allocation_id = aws_eip.nat[count.index].id
#   subnet_id     = aws_subnet.public[count.index].id
#   TODO: Complete this resource
# }

# ============================================================
# ROUTE TABLES
# TODO: Candidate completes route table design
# ============================================================

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.production.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
  tags = {
    Name = "tilington-${var.environment}-public-rt"
  }
}

# TODO: Private route tables (one per AZ pointing to NAT GW)

# ============================================================
# VPC FLOW LOGS — Required for FCA audit trail
# TODO: Candidate configures flow log destination
# ============================================================

resource "aws_flow_log" "main" {
  vpc_id          = aws_vpc.production.id
  traffic_type    = "ALL"
  # TODO: Configure IAM role and CloudWatch log group or S3 destination
  # iam_role_arn    = aws_iam_role.flow_logs.arn
  # log_destination = aws_cloudwatch_log_group.flow_logs.arn
  tags = {
    Name = "tilington-${var.environment}-flow-logs"
  }
}

# ============================================================
# SECURITY GROUPS — STARTER
# TODO: Candidate adds missing security groups
# ============================================================

resource "aws_security_group" "alb" {
  name        = "tilington-${var.environment}-alb-sg"
  description = "Security group for Application Load Balancer"
  vpc_id      = aws_vpc.production.id

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "HTTPS from internet"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow all outbound"
  }

  tags = {
    Name = "tilington-${var.environment}-alb-sg"
  }
}

# TODO: Add security group for EKS nodes
# TODO: Add security group for Aurora PostgreSQL
# TODO: Add security group for internal services
# Each must follow least-privilege: no 0.0.0.0/0 ingress except ALB SG

