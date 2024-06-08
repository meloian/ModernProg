resource "aws_sns_topic" "example" {
  name = "example-topic"
}

resource "aws_sns_topic_subscription" "example" {
  topic_arn = aws_sns_topic.example.arn
  protocol  = "lambda"
  endpoint  = var.lambda_function_arn
}

resource "aws_lambda_permission" "allow_sns" {
  statement_id  = "AllowExecutionFromSNS"
  action        = "lambda:InvokeFunction"
  function_name = var.lambda_function_arn
  principal     = "sns.amazonaws.com"
} 