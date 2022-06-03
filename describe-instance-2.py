#!/usr/bin/python3
import boto3
import sys

try:
    nregion = sys.argv[1]

except:
    print ("Example: ./describe-address.py accessKey secretKey region")
    sys.exit(1)

client = boto3.client('ec2', region_name=nregion)
responsedx = client.describe_instances()
for v in responsedx['Reservations']:
 for printout in v['Instances']:
  for printname in printout['Tags']:
    if printname['Key'] == 'Name':
        name = printname['Value']
  print(name) 
