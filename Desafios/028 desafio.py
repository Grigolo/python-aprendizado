'''
Escreva um programa que faça o computador pensar em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu
'''

import random
from time import sleep

numberSorteado = random.randint(0, 5)
print("Numero: {}" .format(numberSorteado))

n = int(input("O computador pensou em um número entre 0 e 5. Digite um número para ver se você acertou: "))
print("Processando...")
sleep(2)
if numberSorteado == n:
    print("Parabéns você digitou o mesmo número {} que o computador pensou! :)".format(numberSorteado))

else:
    print("Continue tentando o número {} está errado, computador {} ".format(n, numberSorteado))
