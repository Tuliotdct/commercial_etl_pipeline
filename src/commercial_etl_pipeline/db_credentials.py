import boto3
import json
import os
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

def get_secret():

    secret_name = os.getenv('secret_name')
    region_name = os.getenv('region_name')
    profile_name = os.getenv('profile_name')

    if not all([secret_name, region_name, profile_name]):
        raise ValueError("Missing one or more required environment variables: secret_name, region_name, profile_name")


    session = boto3.session.Session(profile_name=profile_name)
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = json.loads(get_secret_value_response['SecretString'])

    return secret
