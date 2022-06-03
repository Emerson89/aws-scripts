#!/usr/bin/python3
import boto3
import sys

try:
    nregion = sys.argv[1]

except:
    print ("Example: ./get-alarms.py region")
    sys.exit(1)

client = boto3.client('cloudwatch', region_name=nregion)
responsedx = client.describe_alarms()
for x in responsedx['MetricAlarms']:
        print(x['AlarmName'],'-',x['Threshold'])

