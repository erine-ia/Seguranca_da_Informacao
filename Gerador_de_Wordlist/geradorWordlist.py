import itertools
print('='*60)
print(f'{"GERADOR DE WORDLIST": ^60}')
print('='*60)

cadeia = input('Digite a string que deseja permutar: \n').strip()
permutacoes = []
resultado = itertools.permutations(cadeia, len(cadeia))

for i in resultado:
    p = (''.join(i))
    permutacoes.append(p)

print(permutacoes)