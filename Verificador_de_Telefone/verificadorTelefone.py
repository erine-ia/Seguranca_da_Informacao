import phonenumbers
from phonenumbers import geocoder

fone = input('Digite o telefone no formato: +551122222222: ')
try:
    phone_number = phonenumbers.parse(fone)
    print(geocoder.description_for_number(phone_number, 'pt'))

except Exception as erro:
    print(erro)












