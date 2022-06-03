#!/usr/bin/python3.8
import sys
import datetime
import boto3
import json
try:
    nregion = sys.argv[1]

except:
    print ("Example: rds-discovery.py REGION")
    sys.exit(1)

def statusvif():
    client = boto3.client('rds', region_name=nregion)
    responsedx = client.describe_db_instances()
    services = []
    for v in responsedx['DBInstances']:
            services.append({"{#DEVICENAME}": v['DBInstanceIdentifier']})
    raw = {"data": services}
    print(json.dumps(raw))

statusvif()


