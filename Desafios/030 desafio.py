'''
Crie um programa que leia um número
e mostre se ele é PAR ou ÍMPAR
'''

numero = int(input("Digite um número para Saber se é Par ou Ímpar: "))

if numero % 2 == 0:
    print("Número {} é Par.".format(numero))
else:
    print("Número {} é Ìmpar.".format(numero))
