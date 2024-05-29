provider "aws" {
  access_key = "mock_access_key"
  secret_key = "mock_secret_key"
  region     = "us-east-1"
  s3_use_path_style = true

  endpoints {
    s3     = "http://localhost:4566"
    lambda = "http://localhost:4566"
    sts    = "http://localhost:4566"
    iam    = "http://localhost:4566"
  }
}

module "s3" {
  source = "./modules/s3"
}

module "iam" {  
  source = "./modules/iam"
}

module "lambda" {
  source = "./modules/lambda"
  start_bucket = module.s3.start_bucket_name
  finish_bucket = module.s3.finish_bucket_name
  iam_role_arn = module.iam.lambda_execution_role_arn  
} 