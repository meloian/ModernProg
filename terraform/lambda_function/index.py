import boto3
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    s3 = boto3.client('s3')
    source_bucket = os.environ['start_bucket']
    destination_bucket = os.environ['finish_bucket']

    for record in event['Records']:
        if 'Sns' in record:
            message = record['Sns']['Message']
            logger.info(f"Received SNS message: {message}")
        elif 's3' in record:
            key = record['s3']['object']['key']
            copy_source = {'Bucket': source_bucket, 'Key': key}
            s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=key)
            logger.info(f"Copied {key} from {source_bucket} to {destination_bucket}")
        else:
            logger.warning(f"Unhandled event type: {record}")

    return 'Done' 