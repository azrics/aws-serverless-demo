variable "aws_region" {

  default = "ap-south-1"
}

variable "bucket_name" {

  default = "student-upload-demo-001"
}

variable "table_name" {

  default = "uploaded_files"
}

variable "lambda_name" {

  default = "document_processor"
}