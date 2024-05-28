import boto3
from botocore.config import Config

localstack_config = Config(
    region_name='us-east-1',
    signature_version='v4',
    retries={'max_attempts': 10, 'mode': 'standard'}
)

s3_client = boto3.client('s3', config=localstack_config, endpoint_url='http://localhost:4566')

s3_client.upload_file(
    Filename='C:/Users/RocK4/Desktop/kpi/ModernProg/terraform/lambda_function/requirements.txt',
    Bucket='s3-start',
    Key='requirements.txt'
)

print("File successfully uploaded to S3 bucket")

response = s3_client.list_objects_v2(Bucket='s3-start')
if 'Contents' in response:
    print("Files in bucket 's3-start':") 
    for obj in response['Contents']:
        print(obj['Key'])
else:
    print("Bucket is empty or file not found") 