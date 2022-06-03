#!/bin/python3
import boto3
import json
import datetime
import sys

try:
    nregion = sys.argv[1]

except:
    print ("Example: directdiscovery.py REGION")
    sys.exit(1)

def statusvif():
    client = boto3.client('directconnect', region_name=nregion)
    responsedx = client.describe_virtual_interfaces()
    services = []
    for v in responsedx['virtualInterfaces']:
            services.append({"{#DEVICENAME}": v['virtualInterfaceName']})
    raw = {"data": services}
    print(json.dumps(raw))

statusvif()