import hashlib


print('='*60)
print(f"{'GERADOR DE HASH':^60}")
print('='*60)
menu = int(input("""
Digite o numero de hash a ser gerado:
[1] MD5
[2] SHA1
[3] SHA256
[4] SHA512
"""))


if menu == 1:
    cadeia = input('Digite o texto a ser gerado uma hash: \n')
    resultado  = hashlib.md5(cadeia.encode('UTF-8'))
    print(f'A hash MD5 de "{cadeia}" é :\n\t{resultado.hexdigest()}')

elif menu == 2:
    cadeia = input('Digite o texto a ser gerado uma hash')
    resultado = hashlib.sh1(cadeia.encode('UTF-8'))
    print(f'A hash sha1 de "{cadeia}" é :\n\t{resultado.hexdigest()}')

elif menu == 3:
    cadeia = input('Digite o texto a ser gerado uma hash')
    resultado  = hashlib.sha256(cadeia.encode('UTF-8'))
    print(f'A hash sha256 de "{cadeia}" é :\n\t{resultado.hexdigest()}')

elif menu == 4:
    cadeia = input('Digite o texto a ser gerado uma hash')
    resultado  = hashlib.sha512(cadeia.encode('UTF-8'))
    print(f'A hash sha512 de "{cadeia}" é :\n\t{resultado.hexdigest()}')

else:
    print('Tente Novamente')
