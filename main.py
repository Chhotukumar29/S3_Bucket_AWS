import boto3
import os

# Initialize a session using Amazon S3
s3 = boto3.client('s3')

bucket_name = 'testbuck'
local_file_path = "C:/Users/KPK/Downloads/Compressed/Financial Data/Currencies/AUD.csv"
s3_file_name = 'AUD.csv'

# uploading the data to S3 bucket
s3.upload_file(local_file_path, bucket_name, s3_file_name)

print(f'Uploaded {local_file_path} to s3://{bucket_name}/{s3_file_name}')

