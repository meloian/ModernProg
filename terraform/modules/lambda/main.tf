resource "aws_lambda_function" "my_lambda" {
  function_name = "my_lambda"
  handler       = "index.handler"
  runtime       = "python3.8"
  role          = var.iam_role_arn

  filename = "${path.module}/lambda_function_payload.zip"
  source_code_hash = filebase64sha256("${path.module}/lambda_function_payload.zip")

  environment {
    variables = {
      start_bucket = var.start_bucket
      finish_bucket = var.finish_bucket
    }
  }
}

resource "aws_lambda_permission" "allow_s3" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.my_lambda.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = "arn:aws:s3:::${var.start_bucket}"
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = var.start_bucket

  lambda_function {
    lambda_function_arn = aws_lambda_function.my_lambda.arn
    events              = ["s3:ObjectCreated:*"]
  }
} 