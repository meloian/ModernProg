output "start_bucket_name" {
  value = aws_s3_bucket.start_bucket.bucket
}

output "finish_bucket_name" {
  value = aws_s3_bucket.finish_bucket.bucket
}