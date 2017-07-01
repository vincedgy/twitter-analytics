#!/usr/bin/env python
"""
create-aws-assets.py

Simple script to create AWS Assets :
    - a kinesis stream
    - a dynamoDB table
    - an S3 bucket

"""
from __future__ import print_function  # Python 2/3 compatibility
import boto3
from botocore.exceptions import ClientError
import logging

# Logging setting
LOGGING_LEVEL = 'INFO'
logging.basicConfig(
    level = getattr(logging, LOGGING_LEVEL),
    format = '%(asctime)s %(name)-8s %(levelname)-8s %(message)s',
    datefmt = '%Y-%m-%d %I:%M:%S %p'
)

# AWS setting
AWS_REGION = 'eu-west-1'
AWS_ACCOUNT = boto3.client('sts').get_caller_identity()['Account']
S3_BUCKET_NAME = AWS_ACCOUNT + '-' + AWS_REGION +'-tweets'
KINESIS_STREAM = 'tweets'
DYNAMODB_TABLE = 'tweetos'

# Kinesis stream creation
try:
    kinesis = boto3.client('kinesis', region_name=AWS_REGION)
    response = kinesis.create_stream(
    StreamName=KINESIS_STREAM,
    ShardCount=1
    )
except ClientError as ex:
    if ex.response['Error']['Code'] == 'AlreadyExists':
        logging.info('Kynesis stream ' + KINESIS_STREAM + ' already exists.')

# DynamoDB table creation
try:
    dynamodb = boto3.client('dynamodb', region_name=AWS_REGION)
    table = dynamodb.create_table(
                        TableName=DYNAMODB_TABLE,
                        KeySchema=[{'AttributeName': 'ScreenName', 'KeyType': 'HASH'}],
                        AttributeDefinitions=[{'AttributeName': 'ScreenName', 'AttributeType': 'S'}],
                        ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
                        )
except ClientError as ex:
    if ex.response['Error']['Code'] == 'AlreadyExists':
        logging.info('DynamoDB table ' + DYNAMODB_TABLE + ' already exists.')

# S3 bucket creation
# Search if S3 bucket exists, and create it if necessary
s3 = boto3.client('s3', region_name=AWS_REGION)
need_to_create_bucket = True
for bucket in s3.buckets.all():
    if bucket == S3_BUCKET_NAME:
        need_to_create_bucket = False
        break
if need_to_create_bucket:
    try:
        s3.create_bucket(S3_BUCKET_NAME)
    except ClientError as ex:
    if ex.response['Error']['Code'] == 'AlreadyExists':
        logging.info('S3 bucket ' + S3_BUCKET_NAME + ' already exists.')
