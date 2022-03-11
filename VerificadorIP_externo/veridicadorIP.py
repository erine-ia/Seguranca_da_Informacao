import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'
resposta = urlopen(url)
dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do Ip externo: \n')
print(f' Ip: {ip}\n Região: {regiao}\n País: {pais}\n Cidade: {cid}\n')