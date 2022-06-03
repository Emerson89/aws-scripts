#!/usr/bin/python3
import boto3
import sys
import csv

try:
    nregion = sys.argv[1]

except:
    print ("Example: ./get-elb.py region")
    sys.exit(1)


client = boto3.client('ec2', region_name=nregion)
responsedx = client.describe_snapshots(
    Filters=[
        {
            'Name': 'owner-id',
            'Values': [
                '686759130677',
            ]
        },
    ],
)
for x in responsedx['Snapshots']:
 with open('snaps.csv', 'a') as file:
  w = csv.writer(file, delimiter=';')
  w.writerow([x['SnapshotId'],x['Description'],x['StartTime']])   
print("Relatório gerado")
