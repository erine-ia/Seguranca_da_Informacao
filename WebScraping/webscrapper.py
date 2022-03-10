from bs4 import BeautifulSoup
import requests
site = input('Endereço: ')
site = requests.get(site).content
# objeto site recebendo o conteudo da requisição http do site

soup = BeautifulSoup(site, 'html.parser')
# objeto soup baixando do site o html

print(soup.prettify())
#prettify transforma o html em string e o print exibe essa transformação
