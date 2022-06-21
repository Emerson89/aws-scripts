#!/usr/bin/python3
import boto3
import sys
import csv

try:
    nregion = sys.argv[1]

except:
    print ("Example: ./get-alb.py region")
    sys.exit(1)

def get_target():
    client = boto3.client('route53', region_name=nregion)
    responsedx = client.list_resource_record_sets(
            HostedZoneId="xxxxxxxxxxxxx",
            )

    for v in responsedx['ResourceRecordSets']:
      with open('test.csv', 'a') as file:
       w = csv.writer(file, delimiter=';')
       w.writerow([v['Name']])   
    print("Relatório gerado")

get_target()
