#!/usr/bin/python3
import boto3
import sys
import json

try:
    nregion = sys.argv[1]

except:
    print ("Example: ./get-alb.py region")
    sys.exit(1)

def get_load(services):
    client = boto3.client('elbv2', region_name=nregion)
    responsedx = client.describe_load_balancers()
    services = []
    for x in responsedx['LoadBalancers']:
        services.append({"{#NAMEBALANCE}": x['LoadBalancerName']})
    return services

def get_target(services):
    client = boto3.client('elbv2', region_name=nregion)
    responsedx = client.describe_target_groups()
    services = []
    for x in responsedx['TargetGroups']:
        nomes = x['TargetGroupArn']
        targets = nomes.split(':')
        services.append({"{#TARGET}": targets[5]})

    return services

raw = {"data": get_load(services="") + get_target(services="")}      
print(json.dumps(raw))
