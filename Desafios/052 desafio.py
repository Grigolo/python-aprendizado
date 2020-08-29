'''
Faça um programa que leia
um número inteiro e diga se ele é
ou não um número primo

Número Primo = Divisível por 1 e por ele mesmo
'''
print('/'*8, ' Número Primo Bem-Vindo', '/'*8)
numero = int(input('Digite qual o número: '))

cont = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='') #cor amarelo
        cont += 1
    else:
        print('\033[31m', end='') #cor vermelho

    print(' {}'.format(c), end='')

print('\n\033[mO número {} foi divisíel {} vezes'.format(numero, cont))
if cont == 2:
    print('Por isso ele é Primo')
else:
    print('E por isso ele não é Primo')



