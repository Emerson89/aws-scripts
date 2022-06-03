#!/usr/bin/python3
import boto3
import sys
import csv

try:
    nregion = sys.argv[1]

except:
    print ("Example: ./get-vpc.py region")
    sys.exit(1)


def vpcid():
 session = boto3.Session(profile_name='interaxa')
 client = session.client('ec2', region_name=nregion)
 responsedx = client.describe_vpcs()
 with open('get-vpc.csv', 'w', newline='') as arquivo_csv:
               fieldnames = ['CIDRBLOCK', 'VPCID', 'ONNERID', 'CONTA1']
               escrever = csv.DictWriter(arquivo_csv, delimiter=';', fieldnames=fieldnames)
               escrever.writeheader()
 for x in responsedx['Vpcs']:
  with open('get-vpc.csv', 'a') as file:
   w = csv.writer(file, delimiter=';')
   w.writerow([x['CidrBlock'],x['VpcId'],x['OwnerId']])   
 print("Relatório gerado")

vpcid()

def vpcid2():
 session = boto3.Session(profile_name='default')
 client = session.client('ec2', region_name=nregion)
 responsedx = client.describe_vpcs()
 with open('get-vpc.csv', 'a', newline='') as arquivo_csv:
               fieldnames = ['CIDRBLOCK', 'VPCID', 'ONNERID', 'CONTA2']
               escrever = csv.DictWriter(arquivo_csv, delimiter=';', fieldnames=fieldnames)
               escrever.writeheader()
 for x in responsedx['Vpcs']:
  with open('get-vpc.csv', 'a') as file:
   w = csv.writer(file, delimiter=';')
   w.writerow([x['CidrBlock'],x['VpcId'],x['OwnerId']])   
 print("Relatório gerado")

vpcid2()


