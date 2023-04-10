import requests as Request
import json
import urllib as urllib
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# %%
with open('sprinklr_refresh_token.json', 'r') as j:
    dados = json.load(j)
    re_token = dados.get('refresh_token')
  
# %%
#https://api2.sprinklr.com/{{env}}/oauth/token?client_id={{apikey}}&client_secret={{secret}}&redirect_uri={{redirect_uri}}&grant_type=refresh_token&refresh_token={{refresh-token}}
requestUrl = "https://api2.sprinklr.com/{0}/oauth/token?client_id={1}&client_secret={2}&redirect_uri={3}&grant_type=refresh_token&refresh_token={4}".format('prod2','#############','######################','https://www.sprinklr.com/pt-br/',re_token)
headers = { 
            'Content-Type': 'application/x-www-form-urlencoded'
          }
request = Request.post(requestUrl,headers=headers,verify=False)

request = request.text
if 'error_description' in request:
  # %%
  from selenium import webdriver 
  from selenium.webdriver.common.by import By
  #Biblioteca usada para identificar tahs html e buscar na pág
  from selenium.webdriver.chrome.options import Options
  # Biblioteca usada para escolher se quero ver a aplicação sendo executada ou não
  from selenium.webdriver.chrome.service import Service
  from webdriver_manager.chrome import ChromeDriverManager
  import requests as Re
  import json as json
  from time import sleep
  import urllib3
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


  # %%
  op = Options()
  #Encurtando o nome do import
  op.headless = True
  #Quando o headless receber True a aplicação não é vista, quando é false vemos a aplicação sendo executada

  servico = Service(ChromeDriverManager().install())
  navegador = webdriver.Chrome(options=op ,service=servico)

  # %%
  sleep(3)
  link = "https://prod2.sprinklr.com/ui/oauth/authorize?client_id=###############&response_type=code&redirect_uri=https%3A%2F%2Fwww.sprinklr.com%2Fpt-br%2F"

  navegador.get(url=link)
  navegador.get

  # %%
  sleep(1)
  navegador.find_element('xpath', '/html/body/div[2]/div[3]/div[1]/form/button/span').click()

  # %%
  sleep(1)
  navegador.find_element('xpath', '//*[@id="root"]/div/div/div/section[2]/section/div[1]/div/div/div/div/div/div/form/div[1]/div[1]/input').send_keys('######')
  sleep(1)
  navegador.find_element('xpath', '//*[@id="root"]/div/div/div/section[2]/section/div[1]/div/div/div/div/div/div/form/div[1]/div[2]/button').click()
  sleep(1)
  navegador.find_element('xpath', '//*[@id="root"]/div/div/div/section[2]/section/div[1]/div/div/div/div/div/div[2]/form/div[2]/div[1]/input').send_keys('################')
  sleep(1)
  navegador.find_element('xpath', '//*[@id="root"]/div/div/div/section[2]/section/div[1]/div/div/div/div/div/div[2]/form/div[2]/button').click()

  # %%
  sleep(1)
  navegador.find_element('xpath', '/html/body/form[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div').click()
  sleep(1)
  navegador.find_element('xpath', '/html/body/form[1]/div[2]/div/div[1]/button/span').click()

  # %%
  novaUrl = navegador.current_url
  novaUrl = novaUrl[37:61]
  navegador.close()
  # %%
  #https://api2.sprinklr.com/prod2/oauth/token?client_id={client_id}&client_secret={client_secret}&redirect_uri={redirect_uri}&grant_type={grant_type}&code={code}
  url_request = "https://api2.sprinklr.com/prod2/oauth/token?client_id={0}&client_secret={1}&redirect_uri={2}&grant_type={3}&code={4}".format('#######','#','https://www.sprinklr.com/pt-br/','authorization_code',novaUrl)
  headers = { 
              'Content-Type': 'application/x-www-form-urlencoded'
            }
  request = Re.post(url_request, headers= headers,verify= False )
  request = request.text
  request

  # %%
  
obj_json = json.loads(request)
with open('sprinklr_refresh_token.json', 'w') as j:
    json.dump(obj_json,j)
resp = request
