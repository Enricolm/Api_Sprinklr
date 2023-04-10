import os

import re
import requests as Req
import json
import urllib as urllibb
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pandas as pd
from datetime import datetime


# %%
key = '##########'
secret = '################'
redirect_uri = 'https://www.sprinklr.com/pt-br/'
auth_token='####################'
code = '####################'

# %%
with open('C:\\Users\\enrico.malachini\\Desktop\\Api_SPRINKLR\\sprinklr_refresh_token.json', 'r') as j:
    i = json.load(j)    
    ref_token = (i['access_token'])
    
headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + ref_token,
            'Key': '##########'
          }    



with open('payload3.json', 'r+') as j:
    payload = json.load(j)

request_url = 'https://api2.sprinklr.com/prod2/api/v2/reports/query'
request = Req.post(request_url, json=payload, headers=headers, verify=False)
response = request.text
obj_json3 = json.loads(response)
obj_json3 = (obj_json3['data']['rows'])
colunas = ['Data', 'Sentimento', 'Valor']
dados3 = pd.DataFrame( data = obj_json3,columns= colunas)    
dados3.sort_values(by= ['Data'], na_position= 'last', inplace= True)
dados3.dropna(inplace=True)
dados3.to_csv(('D:\\GD_Projetos\\TIM\\Payload_2023_Janeiro1-16.csv'), sep=';',index=False)

colunas = ['Data', 'Veiculos', 'Valor']
todos_dados = pd.DataFrame(columns= colunas)
i = 0
while i <= 1:
    with open('payload4.json', 'r+') as j:
        payload = json.load(j)
        payload['page'] = i
        
        

    request_url = 'https://api2.sprinklr.com/prod2/api/v2/reports/query'
    request = Req.post(request_url, json=payload, headers=headers, verify=False)
    response = request.text
    obj_json3 = json.loads(response)
    obj_json3 = (obj_json3['data']['rows'])
    colunas = ['Data', 'Veiculos', 'Valor']
    dados3 = pd.DataFrame( data = obj_json3,columns= colunas)    
    todos_dados = pd.concat([todos_dados,dados3])
    dados3.sort_values(by= ['Data'], na_position= 'last', inplace= True)
    dados3.dropna(inplace=True)
    i = i + 1
    
print(todos_dados)
todos_dados.to_csv(('D:\\GD_Projetos\\TIM\\Payload2_2023_Janeiro1-16.csv'), sep=';',index=False)

