# Serverless Architecture

### Task 1: Automated Instance Management Using AWS Lambda and Boto3

#### Objective: In this assignment, you will gain hands-on experience with AWS Lambda and Boto3, Amazon's SDK for Python. You will create a Lambda function that will automatically manage EC2 instances based on their tags.

Task: You're tasked to automate the stopping and starting of EC2 instances based on tags. 

1. Setup:
   - 	Create two EC2 instances.
   -	Tag one of them as `Auto-Stop` and the other as `Auto-Start`.

Instructions:

-	Navigate to the EC2 dashboard and create two new t2.micro instances (or any other available free-tier type).

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/7b01c7c3-c808-46da-8fd8-62ce2cbcf529)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/947d5325-b0c5-4f5b-a091-05fca8fcf358)


-	Tag the first instance with a key `Action` and value `Auto-Stop`.

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/70c861db-4efe-4517-af1d-11d59c5989df)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/a8ef891e-be52-43e5-a2db-7431d3d4e751)

-	Tag the second instance with a key `Action` and value `Auto-Start`.

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/7835561f-b997-4c95-b5d9-04714a204605)

2. Lambda Function Creation:
    -	Set up an AWS Lambda function
    -	Ensure that the Lambda function has the necessary IAM permissions to describe, stop, and start EC2 instances.

Instructions:

2. Lambda IAM Role:

- In the IAM dashboard, create a new role for Lambda.

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/22766393-42e9-4cb0-b575-7c1c09dafa79)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/8c6d61e2-528f-452c-ad45-6ac48feefa98)

- Attach the `AmazonEC2FullAccess` policy to this role. (Note: In a real-world scenario, you would want to limit permissions for better security.)

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/c4b4a887-5bba-4061-810e-0596a5de0741)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/7d5fa76a-59a8-4784-bf35-b35369e9cd8c)


3. Coding:
    -	Using Boto3 in the Lambda function:
    -	Detect all EC2 instances with the `Auto-Stop` tag and stop them.
    -	Detect all EC2 instances with the `Auto-Start` tag and start them.

Instructions

3. Lambda Function:
-	Navigate to the Lambda dashboard and create a new function.
-	Choose Python 3.x as the runtime.
-	Assign the IAM role created in the previous step.

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/96a047f3-1fe2-42aa-8ba4-1d0390a5c9c9)

-	Write the Boto3 Python script to:
    1.	Initialize a boto3 EC2 client.
    2.	Describe instances with `Auto-Stop` and `Auto-Start` tags.
    3.	Stop the `Auto-Stop` instances and start the `Auto-Start` instances.
    4.	Print instance IDs that were affected for logging purposes.
 
```
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

```
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/5c63cc53-a61f-42b5-aad0-c9aa5e44fb1f)

4. Testing:
    -	Manually invoke the Lambda function.
    -	Confirm that the instance tagged `Auto-Stop` stops and the one tagged `Auto-Start` starts.

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/08ea8f0a-3936-4a3e-8f5b-9e1e52ba3b5e)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/b6e3abb2-830b-4b66-80de-7f97a87e223e)


### Task 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

#### Objective: To gain experience with AWS Lambda and Boto3 by creating a Lambda function that will automatically clean up old files in an S3 bucket.

Task: Automate the deletion of files older than 30 days in a specific S3 bucket.

Instructions:
1. S3 Setup:

- Navigate to the S3 dashboard and create a new bucket.
- Upload multiple files to this bucket, ensuring that some files are older than 30 days (you may need to adjust your system's date temporarily for this or use old files).

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/4a03052e-0d1f-472e-98c5-332efeed86ba)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/02f99481-33b9-444a-8e93-f68c90347da1)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/4e693ac8-7f35-4b7b-8e46-6aa4eda4421b)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/af802036-cdd4-4509-bad8-40101a6125f3)


2. Lambda IAM Role:
- In the IAM dashboard, create a new role for Lambda.
- Attach the `AmazonS3FullAccess` policy to this role. (Note: For enhanced security in real-world scenarios, use more restrictive permissions.)

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/aa959863-f6d9-4340-ad6a-674ff000db7d)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/4ac843e3-05f9-412f-94bd-3c6e9bf8ad75)

3. Lambda Function:
- Navigate to the Lambda dashboard and create a new function.
- Choose Python 3.x as the runtime.
- Assign the IAM role created in the previous step.
- Write the Boto3 Python script to:
     1. Initialize a boto3 S3 client.
     2. List objects in the specified bucket.
     3. Delete objects older than 30 days.
     4. Print the names of deleted objects for logging purposes.

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/f7ef010c-df33-4496-8866-8ab0c3f35dd6)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/a985d859-805d-4483-af48-6fd7d6c76a02)

```
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

```

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/244edc4b-3644-45de-8ed5-67d6d8cd4035)

4. Manual Invocation:
- After saving your function, manually trigger it.
- Go to the S3 dashboard and confirm that only files newer than 30 days remain.

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/5ab8487b-0714-4db4-a455-84dfb7603d8c)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/8640f4de-bd10-4b96-907c-552bd6c3cac7)



### Task 3: Automatic EBS Snapshot and Cleanup Using AWS Lambda and Boto3
#### Objective: To automate the backup process for your EBS volumes and ensure that backups older than a specified retention period are cleaned up to save costs.

Task: Automate the creation of snapshots for specified EBS volumes and clean up snapshots older than 30 days.

Instructions:
1. EBS Setup:
- Navigate to the EC2 dashboard and identify or create an EBS volume you wish to back up.
- Note down the volume ID.

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/66238917-5232-4f99-b431-673ff8072e0d)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/4c00a0e7-235e-4ab1-90c7-e84de599c803)

2. Lambda IAM Role:
- In the IAM dashboard, create a new role for Lambda.
- Attach policies that allow Lambda to create EBS snapshots and delete them (`AmazonEC2FullAccess` for simplicity, but be more restrictive in real-world scenarios).

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/e89f49b8-f534-4ebe-9652-da60b8f61872)

3. Lambda Function:
- Navigate to the Lambda dashboard and create a new function.
- Choose Python 3.x as the runtime.
- Assign the IAM role created in the previous step.
- Write the Boto3 Python script to:
     1. Initialize a boto3 EC2 client.
     2. Create a snapshot for the specified EBS volume.
     3. List snapshots and delete those older than 30 days.
     4. Print the IDs of the created and deleted snapshots for logging purposes.

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/4da26a06-b574-4858-9921-e03f48cd1031)

```
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

```
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/476484f9-ffbb-47cd-bbdd-5cf1644f8e87)

4. Manual Invocation:
- After saving your function, either manually trigger it or wait for the scheduled event.
- Go to the EC2 dashboard and confirm that the snapshot is created and old snapshots are deleted.

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/69ced769-93d5-46d1-a0c8-4ea07eec221c)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/4bba0b38-2fa6-40e3-83a3-1fd7e10ad1d2)


### Task 4: Load Balancer Health Checker
#### Objective: Design a Lambda function that checks the health of registered instances behind an Elastic Load Balancer (ELB) and notifies via SNS if any instances are unhealthy.

Instructions:
1. Create a Lambda function.

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/d9e53d0e-c36c-4376-a0e1-060b76db5cde)

2. With Boto3, configure the function to:
   
- Check the health of registered instances behind a given ELB.
- If any instances are found to be unhealthy, publish a detailed message to an SNS topic.

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/81fa5f47-f393-430e-af9c-a41ae8bde3e1)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/ce744ba8-ecc4-4954-b66d-75cdf0312fe3)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/4b2a459f-ddbb-492e-a1e3-85ba40ee684f)
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/c36b3aef-cb5d-4c67-894e-7b0675e98dc3)

```
import boto3
def lambda_handler(event, context):
    # Initialize a Boto3 ELB client
    elb = boto3.client('elbv2')    
    # Initialize a Boto3 SNS client
    sns = boto3.client('sns')
    # Specify the ARN of the SNS topic you created
    sns_topic_arn = 'arn:aws:sns:ap-south-1:295397358094:AJAYSNS'
    # Specify the name of the target ELB
    elb_name = 'arn:aws:elasticloadbalancing:ap-south-1:295397358094:loadbalancer/app/adarsh-neeraj-lb/b75d821e7370c5cd'
    # Describe the target group of the ELB
    target_groups = elb.describe_target_groups(LoadBalancerArn=elb_name)
    
    # Iterate through the target groups
    for target_group in target_groups['TargetGroups']:
        # Describe the registered instances in the target group
        instances = elb.describe_target_health(TargetGroupArn=target_group['TargetGroupArn'])    
        # Check the health of each instance
        for instance in instances['TargetHealthDescriptions']:
            if instance['TargetHealth']['State'] != 'healthy':
                # If an instance is unhealthy, publish a message to the SNS topic
                message = f"Instance {instance['Target']['Id']} behind ELB {elb_name} is unhealthy."
                sns.publish(
                    TopicArn=sns_topic_arn,
                    Message=message,
                    Subject="Unhealthy Instance Alert"
                )
```
![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/d6e7e65c-63b2-493b-9d13-0cf0b598045d)

![image](https://github.com/AdarshIITDH/Serverless-Architecture/assets/60352729/3d174ba7-77d6-45f7-af9a-1efa396cc1f5)









