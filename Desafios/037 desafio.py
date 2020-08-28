'''
Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:

- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal
'''

num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para a conversão:
[ 1 ] Converter para BINÀRIO
[ 2 ] Converter para OCTAL    
[ 3 ] Converter para HEXADECIMAL
''')

opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINÀRIO: {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} Convertido para OCTAL:  {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} Convertido para HEXADECIMAL: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente')
