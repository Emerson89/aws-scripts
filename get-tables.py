#!/usr/bin/python3
import boto3
import sys
import json

try:
    nregion = sys.argv[1]

except:
    print ("Example: ./get-elb.py region")
    sys.exit(1)


client = boto3.client('dynamodb', region_name=nregion)
responsedx = client.list_tables()
services = []
for x in responsedx['TableNames']:
        services.append({"{#TABLENAMES}": x})
    
raw = {"data": services}
print(json.dumps(raw))
