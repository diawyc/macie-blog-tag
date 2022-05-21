
import json
import boto3
import os
import urllib.parse
"""Initialise boto3"""
s3 = boto3.client('s3')
s3_obj = boto3.client('s3')


def handler(event, context):
 # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print(key)
    response = s3.get_object(Bucket=bucket, Key=key)
    s3_clientobj = response
    s3_clientdata = s3_clientobj['Body'].read().decode('utf-8')
    s3clientlist = json.loads(s3_clientdata)
    sev = s3clientlist["detail"]["severity"]["score"]
    buc = s3clientlist["detail"]["resourcesAffected"]["s3Bucket"]["name"]
    print(buc)
    obj = s3clientlist["detail"]["resourcesAffected"]["s3Object"]["key"]
    print(obj)
    if sev == 3:
        response = s3_obj.put_object_tagging(
            Bucket=buc,
            Key=obj,
            Tagging={
                'TagSet': [
                    {
                        'Key': 'Sensitivity',
                        'Value': 'High'
                    }
                ]
            }
        )

    return response

