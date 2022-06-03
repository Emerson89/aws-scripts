#!/usr/bin/python3
from collections import defaultdict
from pyzabbix import ZabbixAPI
import boto3
import sys

url = "http://localhost/api_jsonrpc.php"
user = "Admin"
password = "zabbix"
zabbix_hosts = {}
zabbix_ips = []
zapi = ZabbixAPI(url)
zapi.login(user,password)

host_interface = zapi.hostinterface.get(output=["ip","dns","hostid","error","available"])
for host in host_interface:
    dns = host['dns']
    ip = host['ip']
    hostid = host['hostid']
    if 'Get value from agent failed: cannot connect to' in host['error'] and host['available'] == '2':
        zabbix_ips.append(ip)
        zabbix_hosts[ip] = hostid

def get_aws_instances():
    aws_ip=[]
    regioes = [sys.argv[1]]

    for regiao in regioes:
        ec2 = boto3.resource('ec2', region_name = regiao)

        running_instances = ec2.instances.filter(Filters=[{
            'Name': 'instance-state-name',
            'Values': ['running','shutting-down','stopping','stopped']}])

        for instance in running_instances:
            aws_ip.append(instance.private_ip_address)

            if instance.public_ip_address != None:
                aws_ip.append(instance.public_ip_address)

    return aws_ip


def delete_zabbix_instance(remove_hosts):
    for host in remove_hosts:
        print('Removido: '+ host)
        zapi.host.delete(zabbix_hosts[host])

awsIp = get_aws_instances()
remove_hosts = list(set(zabbix_ips) - set(awsIp))
# # zabbixIp
delete_zabbix_instance(remove_hosts)

print("Funcionando")