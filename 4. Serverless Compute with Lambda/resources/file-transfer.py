import boto3
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    destination_bucket = 'target-bucket-12345'  # Change to your target bucket name
    copy_source = {'Bucket': source_bucket, 'Key': file_key}
    s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=file_key)
    print(f"File {file_key} moved from {source_bucket} to {destination_bucket}")
