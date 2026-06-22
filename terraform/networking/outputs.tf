# ============================================================
# Tilington plc — Terraform Networking Outputs
# ============================================================
# TODO: Candidate adds outputs for all subnet IDs and the VPC ID
# These are consumed by other Terraform modules (EKS, RDS, etc.)
# ============================================================

output "vpc_id" {
  description = "The ID of the VPC"
  value       = aws_vpc.production.id
}

output "vpc_cidr" {
  description = "The CIDR block of the VPC"
  value       = aws_vpc.production.cidr_block
}

output "public_subnet_ids" {
  description = "List of public subnet IDs"
  value       = aws_subnet.public[*].id
}

# TODO: Add outputs for:
# output "private_app_subnet_ids" { ... }
# output "private_data_subnet_ids" { ... }
# output "nat_gateway_ids" { ... }
# output "internet_gateway_id" { ... }

