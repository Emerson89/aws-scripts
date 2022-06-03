#!/usr/bin/python3

import boto3
import sys
import csv

def update_id(ip_instance, sg_id):
    try:
        ec2 = boto3.resource('ec2', 'us-east-1')
        instances = ec2.instances.filter()
        for instance in instances:
          if instance.private_ip_address == ip_instance:
            all_sg_ids = [sg['GroupId'] for sg in instance.security_groups]
            if sg_id not in all_sg_ids:
              all_sg_ids.append(sg_id)
              instance.modify_attribute(Groups=all_sg_ids)
         
        print(f'Host atualizado {ip_instance}')
    except Exception as err:
        print(f'Falha ao atualizar {err}')

with open('hostsids.csv') as file:
    file_csv = csv.reader(file, delimiter=';',lineterminator='\n')
    for [ip,ids] in file_csv:
        update_id(ip_instance=ip,sg_id=ids)