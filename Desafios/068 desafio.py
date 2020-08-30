'''
Faça um programa que jogue par ou ímpar
com o computador.
O jogo só será interrompido quando o jogador perder
Mostrando o total de vitórias consecutivas que ele
conquistou no final do jogo.
'''
from random import randint
print('=-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*30)
soma = quantasJogadas = vitorias = 0
errou = 0

while True:
    if errou == 0:
        valorJogador = int(input('Diga um valor: '))
        valorComputador = randint(0, 9)

        soma = valorJogador + valorComputador
        quantasJogadas += 1
    escolhaJogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]



    if escolhaJogador == 'P':
       errou = 0
       if soma % 2 == 0:
           print('-'*30)
           print(f'Você jogou {valorJogador} e o computador {valorComputador}. Total de {soma} DEU PAR!')
           print('-'*30)
           vitorias += 1
           print('Você  VENCEU!\nVamos jogar novamente...')
           print('=-'*30)
       else:
            print('-'*30)
            print(f'Você jogou {valorJogador} e computador {valorComputador}. Total de {soma} DEU ÍMPAR!')
            print('-'*30)
            break
    elif escolhaJogador == 'I':
        errou = 0
        if soma % 2 == 0:
            print('-'*30)
            print(f'Você jogou {valorJogador} e o computador {valorComputador}. Total de {soma} DEU PAR')
            print('-'*30)
            break
        else:
            print('-'*30)
            print(f'Você jogou {valorJogador} e o computador {valorComputador}. Total de {soma} DEU ÍMPAR')
            print('-'*30)
            vitorias += 1
            print('Você VENCEU!\nVamos jogar novamente...')
            print('=-'*30)
    else:
        print('Opção incorreta. Tente novamente Par ou Ímpar [P/I].')
        errou = 1


print('Você PERDEU!')
print('=-'*30)
print(f'GAME OVER! Você venceu {vitorias} vezes.')


