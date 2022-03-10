import ctypes

atributo_ocultar = 0x02
pasta = input('Digite o caminho da pasta a ser ocultada: ')
retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

if retorno:
    print('O arquivo foi ocultado')
else:
    print('Arquivo não foi ocultado')