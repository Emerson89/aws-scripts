#!/usr/bin/python3
import boto3
import sys

try:
    nregion = sys.argv[1]

except:
    print ("Example: ./script.py region")
    sys.exit(1)


client = boto3.client('ecs', region_name=nregion)
responsedx = client.update_service(
    cluster='cluster-ecs',
    service='service-ecs',
    desiredCount=60,
)