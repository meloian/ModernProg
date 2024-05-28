resource "aws_s3_bucket" "start_bucket" {
  bucket = "s3-start"
}

resource "aws_s3_bucket" "finish_bucket" {
  bucket = "s3-finish"
}

resource "aws_s3_bucket_lifecycle_configuration" "example" {
  bucket = aws_s3_bucket.start_bucket.id

  rule {
    id     = "log"
    status = "Enabled"

    expiration {
      days = 1
    }
  }
}

resource "aws_s3_bucket_acl" "start_bucket_acl" {
  bucket = aws_s3_bucket.start_bucket.bucket
  acl    = "private"
}

resource "aws_s3_bucket_acl" "finish_bucket_acl" {
  bucket = aws_s3_bucket.finish_bucket.bucket
  acl    = "private"
} 