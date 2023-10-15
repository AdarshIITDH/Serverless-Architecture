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



