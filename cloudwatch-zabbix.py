#!/usr/bin/python3

import sys
import datetime
import boto3

try:
    metName = sys.argv[1]
    funcName = sys.argv[2]
    dimName = sys.argv[3].split(",")
    dimValue = sys.argv[4].split(",")
    nameSpace = sys.argv[5]
    region = sys.argv[6]

    if (len(sys.argv) > 7):
      period = int(sys.argv[7])
    else:
      period = 5

    if (sys.argv[3] == "*"):
      dimName=[]
      dimValue=[]

except:
    print(
        "Usage: cloudwatch-zabbix.py MetricName Function DimensionName,DimensionNames DimensionValue,DimensionValues nameSpace Region [period, default=5]")
    print("Example: cloudwatch-zabbix.py CPUUtilization Average InstanceID i-09e5c692fa389da13 us-east-1 10")
    sys.exit(1)

c = boto3.client('cloudwatch', region_name=region)
end = datetime.datetime.utcnow()
start = end - datetime.timedelta(minutes=period)
r = c.get_metric_statistics(
    Namespace=nameSpace,
    MetricName=metName,
    Dimensions=[{
        'Name': dimName[i],
        'Value': dimValue[i]
    }
    for i,_ in enumerate(dimName)],
    StartTime=start,
    EndTime=end,
    Period=period*60,
    Statistics=[funcName])
try:
   if (r.get("Datapoints")) == []:
    print (0)
   else:
    print(r.get("Datapoints")[0].get(funcName))
except Exception as e:
    print(e)
