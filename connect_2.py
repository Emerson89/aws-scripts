#!/bin/python3

import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1", user="zabbix", passwd="senha", db="zabbix")

cursor = conn.cursor()

try:
  cursor.execute("select * from task")
  result = cursor.fetchall()
  if result == []:
     print("OK")
  else:
    for x in result:
     print (x)
except Exception as e:
    print("table not exists")
conn.close()