#!/usr/bin/python3
import boto3
import sys
import csv

try:
    nregion = sys.argv[1]

except:
    print ("Example: ./script.py region")
    sys.exit(1)

def update_task(api):
 client = boto3.client('ecs', region_name=nregion)
 update = client.update_service(
    cluster='cluster-ecs',
    service='service-ecs',
    desiredCount=int(api)
 )
with open('numtask.csv') as file:
  file_csv = csv.reader(file)
  for [up] in file_csv:
     update_task(api=up)