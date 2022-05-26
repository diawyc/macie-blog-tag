
import json
import boto3
import os
import urllib.parse
"""Initialise boto3"""
s3 = boto3.client('s3')
s3_obj = boto3.client('s3')
datadic={"CREDIT_CARD_NUMBER":3,"USA_SOCIAL_SECURITY_NUMBER":4,"NAME":2}
type="CREDIT_CARD_NUMBER"
def taglevel(typelist):
    levels=[]
    for i in range(len(typelist)):
        levels.append(datadic[typelist[i]])
    return(max(levels))
    

def handler(event, context):
 # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print(key)
    response = s3.get_object(Bucket=bucket, Key=key)
    s3_clientobj = response
    s3_clientdata = s3_clientobj['Body'].read().decode('utf-8')
    s3clientlist = json.loads(s3_clientdata)
#获取保存敏感数据的S3的信息
    buc = s3clientlist["detail"]["resourcesAffected"]["s3Bucket"]["name"]
    obj = s3clientlist["detail"]["resourcesAffected"]["s3Object"]["key"]
#针对default rule的扫描结果取到所有类型
    sensitiveData=s3clientlist["detail"]["classificationDetails"]["result"]["sensitiveData"]
    categorylist=[]
    typelist=[]
    for i in range(0,len(sensitiveData)):
        categorylist.append(sensitiveData[i]["category"])
        types=sensitiveData[i]["detections"]
        for j in range(0,len(types)):
            typelist.append(types[j]["type"])
        
    
    print('you have some sensitive data in category: ')
    print(categorylist)
    print(typelist)
#判断类型对应客户自定义的tag
    tagkey=os.environ['tagkey']
    valuelevel=taglevel(typelist)
    value=os.environ[('level'+str(valuelevel))]
    print(value)
#为S3中的ojb打上对应的标签
    response = s3_obj.put_object_tagging(
        Bucket=buc,
        Key=obj,
        Tagging={
            'TagSet': [
                {
                    'Key': tagkey,
                    'Value': value
                }
            ]
        }
    )

    return response

