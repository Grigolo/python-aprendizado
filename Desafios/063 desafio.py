'''
Escreva um programa que leia um número n inteiro
qualquer e mostre na tela os n primeiros elementos
de uma sequencia de fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''

print('Sequencia de Fibonacci\n')
num = int(input('Digite um número: '))
cont = 0
fibo = 0
auxAnt = 0
auxAtual = 0

while cont < num:

    if cont > 0:
        fibo = auxAnt + auxAtual
        auxAnt = auxAtual
        auxAtual = fibo
        if cont + 1 < num:
            print(' {} '.format(fibo), end='->')
        elif cont + 1 == num:
            print(' {}'.format(fibo))
    else:
        auxAnt = cont
        auxAtual = cont + 1
        print('{} -> {} '.format(auxAnt, auxAtual), end='->')
        cont += 1
    cont += 1
