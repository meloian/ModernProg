variable "start_bucket" {
  description = "Name of the start S3 bucket"
  type        = string
}

variable "finish_bucket" {
  description = "Name of the finish S3 bucket"
  type        = string
}

variable "iam_role_arn" { 
  description = "ARN of the IAM role for Lambda"
  type        = string
} 