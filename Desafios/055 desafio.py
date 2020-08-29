'''
Faça um programa que leia o peso de
cinco pessoas. No final mostre qual
foi o maior e o menor peso lidos.
'''

contMaior = 0
contMenor = 1000

for peso in range(0, 5):
    pesoLido = float(input('Digite o Peso da Pessoa: '))
    if pesoLido > contMaior:
        contMaior = pesoLido
    if pesoLido < contMenor:
        contMenor = pesoLido
print('O Maior Peso Lido é: {}'.format(contMaior))
print('O menor Peso: {}'.format(contMenor))
