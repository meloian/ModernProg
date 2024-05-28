import boto3
import os

def handler(event, context):
    s3 = boto3.client('s3')
    source_bucket = os.environ['start_bucket']
    destination_bucket = os.environ['finish_bucket']

    for record in event['Records']:
        key = record['s3']['object']['key']
        copy_source = {'Bucket': source_bucket, 'Key': key}
        s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=key)

    return 'Done' 