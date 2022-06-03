#!/usr/bin/python3
import boto3
import sys
import csv

try:
    #accessKey = sys.argv[1]
    #secretKey = sys.argv[2]
    nregion = sys.argv[1]

except:
    print ("Example: ./put-parameter.py accessKey secretKey region")
    sys.exit(1)

def create_paramenter(name, value, tipo):
  try:  
   client = boto3.client('ssm', region_name=nregion)
   client.put_parameter(
     Name=name,
     Value=value,
     Type=tipo
   )
   print(f'Parameter cadastrado {name}')
  except Exception as NameError:
   print(f'Parameter já cadastrado {name}')
  except Exception as err:
   print(f'Falha ao cadastrar {err}')  

with open('get-parameter-1.csv') as file:
    file_csv = csv.reader(file, delimiter=';')
    for [nome,values,tipos] in file_csv:
        create_paramenter(name=nome,value=values,tipo=tipos)