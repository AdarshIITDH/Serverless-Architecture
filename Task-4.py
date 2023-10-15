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