'''
3. Lambda Function:
•	Navigate to the Lambda dashboard and create a new function.
•	Choose Python 3.x as the runtime.
•	Assign the IAM role created in the previous step.
•	Write the Boto3 Python script to:
1.	Initialize a boto3 EC2 client.
2.	Describe instances with `Auto-Stop` and `Auto-Start` tags.
3.	Stop the `Auto-Stop` instances and start the `Auto-Start` instances.
4.	Print instance IDs that were affected for logging purposes.
'''

import json
import boto3
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    # Describe instances with 'Auto-Stop' and 'Auto-Start' tags
    def describe_instances(tag_key):
        instances = ec2.describe_instances(Filters=[{'Name': 'tag:Action', 'Values': [tag_key]}])
        return instances['Reservations']
    def manage_instances(tag_key, action):
        instances = describe_instances(tag_key)
        for reservation in instances:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                if action == 'stop':
                    ec2.stop_instances(InstanceIds=[instance_id])
                    print(f"Stopping instance with ID: {instance_id}")
                elif action == 'start':
                    ec2.start_instances(InstanceIds=[instance_id])
                    print(f"Starting instance with ID: {instance_id}")
    manage_instances('Auto-Stop', 'stop')
