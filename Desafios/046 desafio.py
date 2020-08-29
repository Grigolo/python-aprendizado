'''
Faça um programa que mostre na tela
um contagem regressiva para o estouro
de fogos de artifícios, indo do 10 até
0, com uma pausa de 1 segundo entre eles
'''

from time import sleep

for tempo in range(10, -1, -1):
    print(tempo)
    sleep(1)
print('Terminou')