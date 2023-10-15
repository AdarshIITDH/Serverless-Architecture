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







