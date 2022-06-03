#!/bin/python3

import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1", user="zabbix", passwd="senha", db="zabbix")

exists = True
cursor = conn.cursor()

try:

  cursor.execute("select * from xxx")
except Exception as e:
    exists = False
    print("Tabela Não existe")
if exists == True:
    result = cursor.fetchall()
    for x in result:
     print (x)

conn.close()