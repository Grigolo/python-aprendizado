'''
Escreva um programa que leia doi números
inteiros e compare-os mostrando na tela
uma mensagem:

O primeiro valor é maior
O segundo valor é maior
Não existe valor maior. os dois são iguais
'''
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print('O primeiro valor {} é maior'.format(n1))
elif n2 > n1:
    print('O segundo valor {} é maior'.format(n2))
elif n1 == n2:
    print('Não existe valor maior. os dois são iguais: primeiro valor: {} segundo valor: {}'.format(n1, n2))
