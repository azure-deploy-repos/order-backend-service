import boto3

sqs = boto3.client("sqs", region_name="us-east-1")

QUEUE_URL = "YOUR_SQS_URL"

def send_message(message):
    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=message
    )
