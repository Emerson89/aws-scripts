#!/bin/python3
import boto3
import sys
import csv

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
    Filters=[
        {
            'Name': 'tag:Name'
        }
    ]
    with open('instances.csv', 'a') as file:
        w = csv.writer(file, delimiter=';')
        w.writerow([printname['Value'],printout['PrivateIpAddress']])
    print("Relatório gerado")