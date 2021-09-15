""" delete_queue.py: using boto3, search queue list and delete all """
import os

import boto3


sqs_client = boto3.client(
    "sqs",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)


prefix = "asdf"
response = sqs_client.list_queues(QueueNamePrefix=prefix, MaxResults=200)  # max 1000

queues = response["QueueUrls"]

for qq in queues:
    resp = sqs_client.delete_queue(QueueUrl=qq)
    print(f"XXX: deleted: {qq}")
    if resp["ResponseMetadata"]["HTTPStatusCode"] != 200:
        print(f"failed: {qq}")
