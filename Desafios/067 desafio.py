'''
Faça um programa que mostre a tabuada de vários números
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado
for negativo.
'''

condição = False
tabuada = 1
while not condição:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*20)

    if valor < 0:
        break
    else:
        while tabuada <= 10:
            print(f'{valor} X {tabuada} = {valor * tabuada}')
            tabuada += 1
        tabuada = 1
print('Programa de tabuada encerrado. Volte Sempre!')
