#!/usr/bin/python3
import boto3
import sys
import os
import csv

try:
    nregion = sys.argv[1]

except:
    print ("Example: ./script.py region")
    sys.exit(1)

client = boto3.client('ecs', region_name=nregion)
responsedx = client.describe_services(
      cluster='cluster-ecs',
      services=[
           'service-ecs',
      ],
    )
for x in responsedx['services']:
   with open('numtask.csv', 'w') as file:
    w = csv.writer(file)
    num = x['desiredCount']
    count = int(num)
    w.writerow([count])