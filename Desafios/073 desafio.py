'''
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte

Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso
'''

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

indice = int(input('Digite um número entre 0  e  20: '))
condicao = False
while not condicao:

    if indice < 0:
        while indice < 0:
            indice = int(input('Digite um número entre 0  e 20: '))
    elif indice > 20:
        while indice > 20:
            indice = int(input('Digite um número entre 0 e 20: '))
    else:
        condicao = True
print(f'Você digitou o número {numeros[indice]}')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num >= 20:
        break


