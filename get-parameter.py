#!/usr/bin/python3
import boto3
import sys
import csv

try:
    #accessKey = sys.argv[1]
    #secretKey = sys.argv[2]
    nregion = sys.argv[1]
    names = sys.argv[2]

except:
    print ("Example: ./get-parameter.py accessKey secretKey region")
    sys.exit(1)

client = boto3.client('ssm', region_name=nregion)
responsedx = client.get_parameters_by_path(
    Path=names,
    WithDecryption=True,
    ParameterFilters=[
        {
            'Key': 'Name',
            'Values': ['Value']
        },
    ]
)
for v in responsedx['Parameters']:
 with open('get-parameter.csv', 'a') as file:
   w = csv.writer(file, delimiter=';')
   w.writerow([v['Name'],v['Value'],v['Type']])   
print("Relatório gerado")