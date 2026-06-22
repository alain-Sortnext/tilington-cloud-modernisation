# ============================================================
# Tilington plc — Terraform EKS Module
# STATUS: INCOMPLETE — Candidate completes in Phase 4/5
# ============================================================

# EKS Cluster
resource "aws_eks_cluster" "tilington" {
  name     = "tilington-${var.environment}-eks"
  role_arn = aws_iam_role.eks_cluster.arn
  version  = var.kubernetes_version

  vpc_config {
    subnet_ids              = var.private_app_subnet_ids  # Worker nodes in private subnets
    endpoint_public_access  = false  # NCSC Principle 11 — no public API server
    endpoint_private_access = true
    security_group_ids      = [aws_security_group.eks_cluster.id]
  }

  enabled_cluster_log_types = [
    "api", "audit", "authenticator", "controllerManager", "scheduler"
  ]

  encryption_config {
    provider {
      key_arn = var.kms_key_arn
    }
    resources = ["secrets"]
  }

  depends_on = [
    aws_iam_role_policy_attachment.eks_cluster_policy,
  ]

  tags = {
    Name = "tilington-${var.environment}-eks"
  }
}

# TODO: Candidate adds:
# - EKS Managed Node Group(s)
# - OIDC Provider (required for IRSA)
# - aws-load-balancer-controller addon
# - EBS CSI driver addon
# - CoreDNS and kube-proxy addons
# - Cluster autoscaler Helm release

variable "environment" { type = string }
variable "kubernetes_version" { type = string; default = "1.29" }
variable "private_app_subnet_ids" { type = list(string) }
variable "kms_key_arn" { type = string }

resource "aws_iam_role" "eks_cluster" {
  name = "tilington-${var.environment}-eks-cluster-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "eks.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "eks_cluster_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role       = aws_iam_role.eks_cluster.name
}

resource "aws_security_group" "eks_cluster" {
  name        = "tilington-${var.environment}-eks-cluster-sg"
  description = "EKS cluster security group"
  vpc_id      = var.vpc_id  # TODO: Add vpc_id variable
  # TODO: Candidate adds ingress rules
}

