import json
import boto3
from datetime import datetime, timedelta
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    # Get the current date
    current_date = datetime.now()
    # Calculate the date 30 days ago
    thirty_days_ago = current_date - timedelta(days=30)
    objects = s3.list_objects(Bucket='adarsh-bucket')
    object_list = [obj['Key'] for obj in objects['Contents']]  # print(object_list)
    if 'Contents' in objects:
        for obj in objects['Contents']:
            object_key = obj['Key']
            # Get object metadata tags
            metadata = s3.head_object(Bucket='adarsh-bucket', Key=object_key)
            metadata_tags = metadata.get('Metadata', {})
            # print(f"Object Key: {object_key}")        
            if 'last-modified' in metadata_tags:
                last_modified_date = datetime.strptime(metadata_tags['last-modified'], '%Y-%m-%d')     
                # Check if the tag value indicates a date older than 30 days
                if last_modified_date < thirty_days_ago:
                    # Delete the object
                    s3.delete_object(Bucket='adarsh-bucket', Key=object_key)
                    print(f"Deleted object: {object_key}")
            if metadata_tags:
                print("Metadata Tags:")
                for key, value in metadata_tags.items():
                    print(f"  {key}: {value}")
