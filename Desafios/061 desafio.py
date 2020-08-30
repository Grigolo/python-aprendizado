'''
Refaça o Desafio 51.
lendo o primeiro termo e a razão de uma PA.
Mostrando os 10 primeiros termos da Progressão usando a estrutura while.
'''
from datetime import datetime

primeiroTermo = int(input('Digite qual o Primeiro Termo da PA: '))
razao = int(input('Digite qual a razão da PA: '))

#resolução Jeferson
listaPa = '{} '.format(primeiroTermo)
prox = 0
proxTermo = primeiroTermo + razao
listaPa += ' {} '.format(proxTermo)

for pa in range(2, 10):
    prox = proxTermo
    proxTermo = prox + razao
    listaPa += '{} '.format(proxTermo)

print('Lista da PA: ')
print(listaPa)

print('\nWhile Fersontec')
cont = 0
lista = 0
while cont < 10:
    if cont > 0:
        lista += razao
        print(' {} '.format(lista), end='->')
    else:
        lista += primeiroTermo
        print(' {} '.format(lista), end='->')
    cont += 1


#resolução Professor Guanabarra
print('='*10)
print(' '*5, 'Professor Progressão Aritmética')
print('='*10)

décimo = primeiroTermo + (10 - 1) * razao
print('Décimo antes do For: {}'.format(décimo))

for c in range(primeiroTermo, décimo + razao, razao):
    print(' {} '.format(c), end='-> ')


print('Acabou')
