'''
Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar.
Mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint
computador = randint(0, 10)

jogador = int(input('Jogo da Advinhação com o Computador!!!\nEscolha um número entre 0 e 10: '))

cont = 1 #contar quantas vezes jogador tentou

while computador != jogador:
    jogador = int(input('Tente novamente, esolha outro númeroe entre 0 e 10: '))
    cont += 1

print('Deu certo.')
print('Escolhas do computador: {} jogador: {}, você acertou com {} tentativas'.format(computador, jogador, cont))

# Resolução Professor
computador = randint(0, 10)
print('Sou seu Computador...Acabei de pensar em um número entre  0 e 10.')
print('Será que você consegue adivinhar qual foi? ')

acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu Palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
