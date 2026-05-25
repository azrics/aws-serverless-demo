output "bucket_name" {

  value = aws_s3_bucket.uploads.bucket
}



output "lambda_name" {

  value = aws_lambda_function.processor.function_name
}



output "table_name" {

  value = aws_dynamodb_table.files.name
}