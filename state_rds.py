#!/bin/python3
import boto3
import sys

instanceid = sys.argv[1]
nregion = sys.argv[2]

def statusvif():
    client = boto3.client('rds', region_name=nregion)
    responsedx = client.describe_db_instances()
    for v in responsedx['DBInstances']:
     if v['DBInstanceIdentifier'] == instanceid:
        filtredInstance = v
    ConnectionState = filtredInstance['DBInstanceStatus']
    traductionDict = {"available" : 1, "stopped": 2, "failed": 3, "deleting": 4, "rebooting": 5, "maintenance": 6, "modifying": 7, "restore-error": 8, "stopping": 9, "storage-optimization": 10}
    print(traductionDict.get(ConnectionState))

statusvif()