# ============================================================
# Tilington plc — Terraform IAM / Security Module
# AWS Cloud Modernisation Programme
# ============================================================
# STATUS: INCOMPLETE — Candidate completes in Phase 4
# ============================================================

# ============================================================
# KMS — Customer Managed Keys
# One CMK per data classification
# ============================================================

resource "aws_kms_key" "production_data" {
  description             = "Tilington production data encryption key"
  deletion_window_in_days = 30
  enable_key_rotation     = true

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "Enable IAM User Permissions"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        }
        Action   = "kms:*"
        Resource = "*"
      }
      # TODO: Candidate adds key policy statements for:
      # - Aurora PostgreSQL service role
      # - EKS node role
      # - CloudTrail service
      # Follow least-privilege: each service only gets the actions it needs
    ]
  })

  tags = {
    Name           = "tilington-production-data-key"
    DataClass      = "Restricted"
    GDPRInScope    = "true"
  }
}

resource "aws_kms_alias" "production_data" {
  name          = "alias/tilington-production-data"
  target_key_id = aws_kms_key.production_data.key_id
}

# TODO: Add KMS key for audit logs
# resource "aws_kms_key" "audit_logs" { ... }

# TODO: Add KMS key for backups
# resource "aws_kms_key" "backups" { ... }

# ============================================================
# IAM — EKS Node Role (STARTER)
# TODO: Candidate reviews and extends permissions
# ============================================================

resource "aws_iam_role" "eks_node" {
  name = "tilington-eks-node-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "ec2.amazonaws.com" }
    }]
  })

  tags = {
    Name = "tilington-eks-node-role"
  }
}

resource "aws_iam_role_policy_attachment" "eks_worker_node" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
  role       = aws_iam_role.eks_node.name
}

resource "aws_iam_role_policy_attachment" "eks_cni" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
  role       = aws_iam_role.eks_node.name
}

resource "aws_iam_role_policy_attachment" "eks_ecr_read" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
  role       = aws_iam_role.eks_node.name
}

# TODO: Candidate adds:
# - EKS cluster role
# - IRSA (IAM Roles for Service Accounts) for microservices
#   Each microservice gets its own IAM role with minimum required permissions
# - CloudTrail write role
# - Terraform execution role with permission boundary

# ============================================================
# CLOUDTRAIL — Audit logging (STARTER)
# ============================================================

resource "aws_cloudtrail" "main" {
  name                          = "tilington-audit-trail"
  s3_bucket_name                = aws_s3_bucket.audit_logs.id
  include_global_service_events = true
  is_multi_region_trail         = true
  enable_log_file_validation    = true
  # TODO: Enable CloudWatch Logs integration
  # cloud_watch_logs_group_arn = ...
  # cloud_watch_logs_role_arn  = ...

  event_selector {
    read_write_type           = "All"
    include_management_events = true

    data_resource {
      type   = "AWS::S3::Object"
      values = ["arn:aws:s3:::tilington-production-*"]
    }
  }

  tags = {
    Name    = "tilington-audit-trail"
    FCAReq  = "true"
    GDPR    = "true"
  }
}

resource "aws_s3_bucket" "audit_logs" {
  bucket = "tilington-audit-logs-${data.aws_caller_identity.current.account_id}"
  # TODO: Candidate adds:
  # - Bucket policy (deny non-CloudTrail writes)
  # - Versioning
  # - Object lock (COMPLIANCE mode — immutable audit logs)
  # - Lifecycle policy (retain 7 years per FCA record-keeping)
  # - KMS encryption
  tags = {
    Name      = "tilington-audit-logs"
    Immutable = "true"
    FCAReq    = "true"
  }
}

# TODO: Add bucket policy to restrict CloudTrail log access
# TODO: Add S3 Object Lock in COMPLIANCE mode

# ============================================================
# GUARDUTY (STARTER — TODO: Enable in all accounts)
# ============================================================

resource "aws_guardduty_detector" "main" {
  enable = true

  datasources {
    s3_logs {
      enable = true
    }
    kubernetes {
      audit_logs {
        enable = true
      }
    }
  }

  tags = {
    Name = "tilington-guardduty"
  }
}

# ============================================================
# DATA SOURCES
# ============================================================

data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

