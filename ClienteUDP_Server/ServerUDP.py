import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com Sucesso!')

host = 'localhost'
porta = 5432

s.bind((host, porta))
mensagem = '\nServidor: Olá Cliente, e aí?'

while 1:
    dados, endereco = s.recvfrom(4896)

    if dados:
        print('Servidor enviando mensagem')
        s.sendto(dados + (mensagem.encode()), endereco)
