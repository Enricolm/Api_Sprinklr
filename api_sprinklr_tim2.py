import requests as Req
import json
import urllib as urllibb
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pandas as pd

# %%
key = '#########'
secret = '##################'
redirect_uri = 'https://www.sprinklr.com/pt-br/'
auth_token='###############'
code = '##################'

# %%
with open('C:\\Users\\enrico.malachini\\Desktop\\Api_SPRINKLR\\sprinklr_refresh_token.json', 'r') as j:
    i = json.load(j)    
    ref_token = (i['access_token'])
    
headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + ref_token,
            'Key': '#########'
          }    

i = 0
colunas = ['Data', 'Veiculos', 'Valor']
todos_dados = pd.DataFrame(columns=colunas)
while i != 10:

    with open('payload2.json', 'r+') as j:
        payload = json.load(j)
        payload['page'] = i

    request_url = 'https://api2.sprinklr.com/prod2/api/v2/reports/query'
    request = Req.post(request_url, json=payload, headers=headers, verify=False)
    response = request.text
    obj_json2 = json.loads(response)
    obj_json2 = obj_json2['data']['rows']
    colunas = ['Data', 'Veiculos', 'Valor']
    dados2 = pd.DataFrame( data = obj_json2, columns= colunas)
    dados2.sort_values(by= ['Data'], na_position= 'last', inplace= True)
    dados2.dropna(inplace=True)
    todos_dados = pd.concat([todos_dados,dados2], ignore_index= True)
    if dados2.shape[0] == 120:
        i = i + 1
    else:
        i = 10

todos_dados.to_csv('D:\\GD_Projetos\\TIM\\sprinklr_veiculos.csv', sep=';',index=False)
print(todos_dados)
with open('C:\\Users\\enrico.malachini\\Desktop\\Api_SPRINKLR\\payload2.json', 'w') as j:
    payload['startTime'] = payload['startTime'] + 86400000 
    payload['endTime'] = payload['endTime'] + 86400000 
    json.dump(payload, j, indent=4)

