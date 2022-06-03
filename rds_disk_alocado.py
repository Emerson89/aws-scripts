#!/bin/python3
import boto3
import sys

instanceid = sys.argv[1]
nregion = sys.argv[2]
accessKey = sys.argv[3]
secretKey = sys.argv[4]

def disk():
    client = boto3.client('rds', aws_access_key_id=accessKey, aws_secret_access_key=secretKey, region_name=nregion)
    responsedx = client.describe_db_instances()
    for v in responsedx['DBInstances']:
     if v['DBInstanceIdentifier'] == instanceid:
        filtredInstance = v
    alocado = filtredInstance['AllocatedStorage']
    print(alocado)
disk()