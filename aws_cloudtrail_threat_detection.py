import boto3
import json

# Initialize clients
s3_client = boto3.client('s3')
cloudtrail_client = boto3.client('cloudtrail')

# Fetch CloudTrail logs from an S3 bucket
bucket_name = "your-cloudtrail-bucket"
prefix = "logs/"
response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

# Analyze logs for suspicious activity
for obj in response.get('Contents', []):
    log_file = obj['Key']
    log_data = s3_client.get_object(Bucket=bucket_name, Key=log_file)['Body'].read()
    events = json.loads(log_data)

    for event in events.get('Records', []):
        if event.get('eventName') == 'DeleteBucket':
            print(f"Alert: Unauthorized bucket deletion attempt by {event['userIdentity']['arn']}")
