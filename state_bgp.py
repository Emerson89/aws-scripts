#!/bin/python3
import boto3
import sys

vifname = sys.argv[1]
nregion = sys.argv[2]

def statusvif():
    client = boto3.client('directconnect',region_name=nregion)
    responsedx = client.describe_virtual_interfaces()
    for v in responsedx['virtualInterfaces']:
     vifname2 = (v['virtualInterfaceName'])
     if vifname == vifname2:
      for bgppeer in v['bgpPeers']:
          ConnectionState = bgppeer['bgpStatus']
      if ConnectionState == "up":
            statevalue = 1
            print (1)
      else:
            statevalue = 0
            print (0)

statusvif()