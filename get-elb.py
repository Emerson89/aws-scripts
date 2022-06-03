#!/usr/bin/python3
import boto3
import sys
import json

try:
    nregion = sys.argv[1]

except:
    print ("Example: ./get-elb.py region")
    sys.exit(1)

def get_load():
    client = boto3.client('elb', region_name=nregion)
    responsedx = client.describe_load_balancers()
    services = []
    for x in responsedx['LoadBalancerDescriptions']:
        services.append({"{#NAMEBALANCE}": x['LoadBalancerName']})

    raw = {"data": services }      
    print(json.dumps(raw))

get_load()