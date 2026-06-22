# ============================================================
# Tilington plc — Terraform Networking Variables
# ============================================================

variable "aws_region" {
  description = "Primary AWS region — must be eu-west-2 for UK data residency"
  type        = string
  default     = "eu-west-2"
  validation {
    condition     = var.aws_region == "eu-west-2"
    error_message = "UK GDPR requires eu-west-2 (London) as primary region."
  }
}

variable "environment" {
  description = "Environment name: production, non-production, shared-services"
  type        = string
  validation {
    condition     = contains(["production", "non-production", "shared-services"], var.environment)
    error_message = "Environment must be production, non-production, or shared-services."
  }
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  # TODO: Candidate chooses appropriate CIDR from Tilington network design
  # Must not conflict with on-premise ranges (DC1: 10.10.0.0/16, DC2: 10.20.0.0/16)
  default = "10.30.0.0/16"
}

variable "public_subnet_cidrs" {
  description = "CIDR blocks for public subnets (one per AZ)"
  type        = list(string)
  default     = ["10.30.1.0/24", "10.30.2.0/24", "10.30.3.0/24"]
}

variable "private_app_subnet_cidrs" {
  description = "CIDR blocks for private application subnets (one per AZ)"
  type        = list(string)
  # TODO: Candidate completes these values
  default     = []
}

variable "private_data_subnet_cidrs" {
  description = "CIDR blocks for private data subnets (one per AZ)"
  type        = list(string)
  # TODO: Candidate completes these values
  default     = []
}

variable "availability_zones" {
  description = "AWS availability zones to use"
  type        = list(string)
  default     = ["eu-west-2a", "eu-west-2b", "eu-west-2c"]
}

variable "nat_gateway_count" {
  description = "Number of NAT Gateways. 1 = cost-optimised, 3 = HA. Document trade-off in ADR."
  type        = number
  default     = 1
  # TODO: Candidate evaluates: for production, 3 NAT GWs recommended for AZ resilience
  # Cost implication: ~£90/month per additional NAT GW
}

