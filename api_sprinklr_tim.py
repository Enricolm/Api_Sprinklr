import requests as Req
import json
import urllib as urllibb
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pandas as pd

# %%
key = '############'
secret = '#################'
redirect_uri = 'https://www.sprinklr.com/pt-br/'
auth_token='#############'
code = '################'

# %%
with open('C:\\Users\\enrico.malachini\\Desktop\\Api_SPRINKLR\\sprinklr_refresh_token.json', 'r') as j:
    i = json.load(j)    
    ref_token = (i['access_token'])
    
headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + ref_token,
            'Key': '############'
          }    



colunas = ['Data', 'Sentimento', 'Valor']
todos_os_dados = pd.DataFrame(columns=colunas)
i = 0
ite = 120    
while ite == 120:
    with open('payload.json', 'r+') as j:
        payload = json.load(j)
        payload['page'] = i

    request_url = 'https://api2.sprinklr.com/prod2/api/v2/reports/query'
    request = Req.post(request_url, json=payload, headers=headers, verify=False)
    response = request.text
    obj_json2 = json.loads(response)
    obj_json2 = obj_json2['data']['rows']
    dados2 = pd.DataFrame( data = obj_json2,columns= colunas)    
    dados2.sort_values(by= ['Data'], na_position= 'last', inplace= True)
    dados2.dropna(inplace=True)
    todos_os_dados = pd.concat([todos_os_dados,dados2])
    ite = dados2.shape[0]
    if ite == 120:
        i = i + 1


todos_os_dados.to_csv('D:\\GD_Projetos\\TIM\\sprinklr_sentimentos.csv', sep=';',index=False)



with open('C:\\Users\\enrico.malachini\\Desktop\\Api_SPRINKLR\\payload.json', 'w') as j:
    payload['startTime'] = payload['startTime'] + 86400000 
    payload['endTime'] = payload['endTime'] + 86400000 
    json.dump(payload, j, indent=4)