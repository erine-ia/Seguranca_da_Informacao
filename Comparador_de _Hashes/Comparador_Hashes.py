import hashlib
arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open('a.txt', 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open('b.txt', 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print(f'O hash do arquivo {arquivo1} é: {hash1.hexdigest()}')
    print(f'O hash do arquivo {arquivo2} é: {hash2.hexdigest()}')

else:
    print(f'Os arquivos {arquivo1} e {arquivo2} são iguais')
    print(f'O hash do arquivo {arquivo1} é: {hash1.hexdigest()}')
    print(f'O hash do arquivo {arquivo2} é: {hash2.hexdigest()}')

#ripemd160 -> algoritmo de hash (como sha1, md5..) de 160bits
#digest resume os dados passados pelo metódo update.