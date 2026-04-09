import boto3

import subprocess

s3 = boto3.resource('s3')

buckets = []

for bucket in s3.buckets.all():
    buckets.append(bucket.name)