import boto3
import base64
from datetime import datetime

s3 = boto3.client('s3')
BUCKET_NAME = 'our-first-bucket-66543'

def lambda_handler(event, context):
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record["kinesis"]["data"])
        print("Decoded payload:", payload)

        # Construct a file name based on the event timestamp and partition key
        partition_key = record['kinesis']['partitionKey']
        timestamp = datetime.utcnow().strftime('%Y-%m-%d-%H%M%S')
        filename = f"{partition_key}-{timestamp}.txt"

        # Put the data into the S3 bucket
        s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=payload)
