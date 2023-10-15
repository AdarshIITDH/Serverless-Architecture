'''
Lambda Function:
Navigate to the Lambda dashboard and create a new function.
Choose Python 3.x as the runtime.
Assign the IAM role created in the previous step.
Write the Boto3 Python script to:
    Initialize a boto3 EC2 client.
    Create a snapshot for the specified EBS volume.
    List snapshots and delete those older than 30 days.
    Print the IDs of the created and deleted snapshots for logging purposes.
'''

import json
import boto3
from datetime import datetime, timedelta, timezone

def lambda_handler(event, context):
    # Initialize a Boto3 EC2 client
    ec2 = boto3.client('ec2')
    # Specify the EBS volume ID for which you want to create a snapshot
    volume_id = 'vol-0bb16ec4917256c7c'
    # Create a snapshot for the specified EBS volume
    snapshot = ec2.create_snapshot(
        VolumeId=volume_id,
        Description=f'Snapshot for EBS volume {volume_id}'
    )
    # Print the snapshot ID for logging purposes
    snapshot_id = snapshot['SnapshotId']
    print(f"Snapshot ID: {snapshot_id}")
    
    # List snapshots for the specified volume
    snapshots = ec2.describe_snapshots(Filters=[{'Name': 'volume-id', 'Values': [volume_id]}])

    # Calculate the date 30 days ago
    thirty_days_ago = datetime.now(timezone.utc) - timedelta(days=30)    
    
    # Iterate through the snapshots
    for snapshot in snapshots['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        snapshot_start_time = snapshot['StartTime']

        # Check if the snapshot is older than 30 days
        if snapshot_start_time < thirty_days_ago:
            # Delete the snapshot
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted Snapshot ID: {snapshot_id}")

    # Return the IDs of the created and deleted snapshots
    return {
        'statusCode': 200,
        'body': {
            'created_snapshot_id': snapshot_id,
            'deleted_snapshot_ids': [snapshot['SnapshotId'] for snapshot in snapshots['Snapshots'] if snapshot['StartTime'] < thirty_days_ago]
        }
    }
