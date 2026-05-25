# aws-serverless-demo

# Prerequisites
Set the following credentials.
- AWS_ACCESS_KEY
- AWS_SECRET_KEY
- AWS_REGION

# What the Infra Contains

The infrastructure deploys:
- `iam` roles to access the services
- `s3` bucket as object storage and the trigger for the lambda
- `lambda` function to use the python code to do the file processing
- `dynamodb` to store the processing results of the lambda function.
- `cloudwatch` stores the logs of the lambda processor