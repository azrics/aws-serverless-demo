resource "aws_lambda_function" "processor" {

  function_name = var.lambda_name

  filename = "../lambda/lambda.zip"

  source_code_hash =
    filebase64sha256("../lambda/lambda.zip")

  handler = "app.lambda_handler"

  runtime = "python3.12"

  role = aws_iam_role.lambda_role.arn

  timeout = 30

  environment {

    variables = {

      TABLE_NAME =
        aws_dynamodb_table.files.name

      ENVIRONMENT = "dev"

      MAX_FILE_SIZE = "5000000"
    }
  }
}