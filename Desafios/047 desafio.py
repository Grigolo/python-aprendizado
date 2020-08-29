'''
Crie um programa que na tela
todos os números pares que estão
no intervalo entre 1 e 50.
'''

#números pares
for pares in range(1, 50):
    if (pares % 2) == 0:
        print('Esse Número {} é par! '.format(pares), end='')
print('Fim Pares')

#numeros impares
for impares in range(1, 50):
    if (impares % 2 ) != 0:
        print('Esse número {} é ímpar!'.format(impares))

print('Fim Impares')