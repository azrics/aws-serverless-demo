import json
import os
import uuid
from datetime import datetime
from urllib.parse import unquote_plus

import boto3


# AWS clients
s3 = boto3.client("s3")

dynamodb = boto3.resource("dynamodb")


# Environment variables
TABLE_NAME = os.environ["TABLE_NAME"]

ENVIRONMENT = os.environ.get(
    "ENVIRONMENT",
    "local"
)

MAX_FILE_SIZE = int(
    os.environ.get(
        "MAX_FILE_SIZE",
        "5000000"
    )
)


table = dynamodb.Table(TABLE_NAME)


def count_words(text):

    words = text.split()

    return len(words)


def create_response(status, message):

    return {

        "statusCode": status,

        "body": json.dumps(
            {
                "message": message
            }
        )
    }


def lambda_handler(event, context):

    try:

        print(
            f"Running in {ENVIRONMENT}"
        )

        print(
            json.dumps(
                event,
                indent=2
            )
        )


        record = event["Records"][0]

        bucket = (
            record["s3"]["bucket"]["name"]
        )

        key = unquote_plus(
            record["s3"]["object"]["key"]
        )

        size = (
            record["s3"]["object"]
            .get("size", 0)
        )


        print(
            f"Bucket: {bucket}"
        )

        print(
            f"Key: {key}"
        )

        print(
            f"Size: {size}"
        )


        if size > MAX_FILE_SIZE:

            print(
                "File exceeds size limit"
            )

            return create_response(
                400,
                "File too large"
            )


        response = s3.get_object(

            Bucket=bucket,

            Key=key
        )


        file_content = (
            response["Body"]
            .read()
        )


        text = file_content.decode(
            "utf-8"
        )


        word_count = count_words(
            text
        )


        print(
            f"Word count: {word_count}"
        )


        item = {

            "id":
            str(uuid.uuid4()),

            "filename":
            key,

            "bucket":
            bucket,

            "word_count":
            word_count,

            "environment":
            ENVIRONMENT,

            "processed_at":
            datetime.utcnow()
            .isoformat()
        }


        table.put_item(
            Item=item
        )


        print(
            "Saved to DynamoDB"
        )


        return create_response(
            200,
            "Processing successful"
        )


    except UnicodeDecodeError:

        print(
            "Non-text file uploaded"
        )

        return create_response(
            400,
            "Upload text files only"
        )


    except Exception as e:

        print(
            f"Error: {str(e)}"
        )

        raise e