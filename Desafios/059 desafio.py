'''
Crie um programa que leia dois valores
e mostre um menu na tela:

[1] Somar
[2] multiplicar
[3] maior
[4] novos valores
[5] sair do programa

Seu programa deverá realizar a operação
solicitada em cada caso
'''

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))

executar = False
while not executar:
    print('*'*10, '\n-----Menu-----', '\nEscolha ação a fazer:')
    print('''
        [1] Somar
        [2] Multiplicar
        [3] Maior valor
        [4] Novos valores
        [5] Sair do Programa''')

    opção = int(input('Qual opção? '))

    if opção == 1:
         print('A soma dos valores {} e {} é: {}'.format(v1, v2, v1 + v2))
    elif opção == 2:
            print('A multiplicação dos valores {} e {} é: {}'.format(v1, v2, v1 * v2))
    elif opção == 3:
        if v1 > v2:
            print('O maior valor entre {} e {} é: {}'.format(v1, v2, v1))
        elif v2 > v1:
            print('O maior valor entre {} e {} é: {}'.format(v1, v2, v2))
        else:
            print('Os dois valores são iguais nenhum é maior')
    elif opção == 4:
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Fim do Programa')
        exit(1)
    else:
        print('Opção incorreta tente outra vez')

