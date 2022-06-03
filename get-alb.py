#!/usr/bin/python3
import boto3
import sys
import json

try:
    nregion = sys.argv[1]
    arnloadbalancer = sys.argv[2]

except:
    print ("Example: ./get-alb.py region")
    sys.exit(1)

def get_target():
    client = boto3.client('elbv2', region_name=nregion)
    responsedx = client.describe_target_groups(
            LoadBalancerArn=arnloadbalancer,
            )
    services = []
    for x in responsedx['TargetGroups']:
        nomes = x['TargetGroupArn']
        targets = nomes.split(':')
        services.append({"{#TARGET}": targets[5]})

    raw = {"data": services}
    print(json.dumps(raw))

get_target()
