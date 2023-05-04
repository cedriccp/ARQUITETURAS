import pythonwin
import pythoncom
import requests
import json
import pandas as pd
import psycopg2
import requests


from datetime import date

data_atual = date.today()
print(data_atual)

data_em_texto = ‘{}/{}/{}’.format(data_atual.day, data_atual.month,
data_atual.year)




""" retorna a horaa e o fuso horario */
https://worldtimeapi.org/api/timezone/America/Sao_Paulo  """

def hora(timezone):
  url = 'http://worldtimeapi.org/api/timezone/America/Sao_Paulo' + timezone
  hora = datetime.fromisoformat(resposta.json()['datetime'])
  return hora

""" Estamos utilizando o método .json() da resposta 
para transformar o resultado em um objeto JSON e 
então acessamos a propriedade datetime deste objeto. 
A função fromisoformat do objeto datetime consegue 
converter uma string de uma data no formato ISO 8601 
em um objeto datetime do python. """







/* As bibliotecas requests e json vão auxiliar na extração dos dados da API. O pacote pandas vai realizar a estruturação de dados. E a biblioteca psycopg2 vai fazer a comunicação com o PostgreSQL */
url        = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
parametros = {}
resposta   = requests.request("GET", url, params=parametros)
objetos    = json.loads(resposta.text)
dados      = objetos['dados']