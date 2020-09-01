'''
Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados
e também indique o menor e o maior valor que estão
na tupla.
'''

from random import randint

listaString = ''
cont = 0
maior = 0
menor = 10000

while True:
    numerosAleatorios = randint(0, 11)
    if cont < 4:
        listaString += str(numerosAleatorios) + ' '
    else:
        listaString += str(numerosAleatorios)
    cont += 1
    if cont == 5:
        break
print(f'Valores lista String: {listaString}')

numerosTuplas = tuple(map(int, listaString.split(' '))) #passando string para tupla

print(f'Nova tupla criada: {numerosTuplas}')

for num in numerosTuplas:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')

# resolução do Professor
print('=-'*10, ' Resolução do Professor')

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram: {numeros}')

print(f'O maior valor é: {max(numeros)}')
print(f'O menor valor é: {min(numeros)}')





