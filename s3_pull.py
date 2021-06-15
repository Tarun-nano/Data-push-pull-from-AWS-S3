
import boto3
import json

def s3_pull():

    client = boto3.client('s3',
                        aws_access_key_id='',
                        aws_secret_access_key=''
                        )
    result = client.get_object(Bucket='karam-dump', Key='karamdump.json') 
    text = result["Body"].read()
    return json.loads(text)

print(s3_pull())