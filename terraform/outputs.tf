output "start_bucket_name" {
  value = module.s3.start_bucket_name
}

output "finish_bucket_name" {
  value = module.s3.finish_bucket_name
}

output "lambda_function_name" {
  value = module.lambda.lambda_function_name
} 