import os

import boto3


session = boto3.Session(profile_name='default')
credentials = session.get_credentials()
os.environ['AWS_ACCESS_KEY_ID'] = credentials.access_key
os.environ['AWS_SECRET_ACCESS_KEY'] = credentials.secret_key

client = boto3.client(
    's3',
    aws_access_key_id=credentials.access_key,
    aws_secret_access_key=credentials.secret_key,
)

'''
boto3 S3 client function

response = client.list_objects(
    Bucket='string',
    Delimiter='string',
    EncodingType='url',
    Marker='string',
    MaxKeys=123,
    Prefix='string',
    RequestPayer='requester',
    ExpectedBucketOwner='string'
)
'''

PREFIX = 'your_key'
BUCKET = 'your_bucket'

paginator = client.get_paginator('list_objects_v2')
pages = paginator.paginate(Bucket=BUCKET, Prefix=PREFIX, Delimiter='/')

for page in pages:
    prefixes = [
        prefix["Prefix"] for prefix in page['CommonPrefixes']
    ]
