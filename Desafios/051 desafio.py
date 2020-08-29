'''
Desenvolva um programa que leia
o primeiro termo e a razão de uma PA (progressão aritmética)
No final, mostre os 10 primeiros termos dessa progressão.
'''

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

#resolução Professor Guanabarra
print('='*10)
print(' '*5, ' Progressão Aritmética')
print('='*10)

décimo = primeiroTermo + (10 - 1) * razao
for c in range(primeiroTermo, décimo + razao, razao):
    print(' {} '.format(c), end='-> ')
print('Acabou')
