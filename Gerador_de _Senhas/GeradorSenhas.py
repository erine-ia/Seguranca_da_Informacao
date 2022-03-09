import random
import string

print('='* 30)
print(f"{'GERADOR DE SENHAS' : ^30}")
print('='*30)


tamanho = int(input('Digite o tamanho que deseja sua senha : '))
chars = string.ascii_letters + string.digits + '!@#$%&*()+'
rnd = random.SystemRandom()


print('')
print('Senha Gerada: ')
print(''.join(rnd.choice(chars) for i in range(tamanho)))
print('-'*30)