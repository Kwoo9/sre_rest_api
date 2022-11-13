import logging
import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region=None):
    # Create bucket
    try:
        s3 = boto3.client('s3', endpoint_url="http://localhost:4566")
        s3.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

bucket_tf = create_s3_bucket('test-bucket')

if bucket_tf:
    print('Success')
else:
    print("Fail")