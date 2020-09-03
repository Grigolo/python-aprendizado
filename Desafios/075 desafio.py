'''
Desenvolva um programa que leia quatro valores
pelo teclado e guarda-os em uma tupla. No final
mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

print('=-'*10, 'Exercícios com Tuplas 75')
qtdNove = 0
qualPosicao = -1
quaisNumerosPares = ''

numeros = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
           int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))

print(f'Valores da Tupla: {numeros}')

for num in numeros:
    if num % 2 == 0:
        quaisNumerosPares += str(num) + ' '
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
#print(f'O número 3 inicialmente apareceu na posição: {qualPosicao}')
print(f'Os números pares da Tupla são: {quaisNumerosPares}')


