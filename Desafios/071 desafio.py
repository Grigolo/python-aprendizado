'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de
R$ 50, R$ 20, R$ 10 e R$ 1.
'''
cedulas50 = cedulas20 = cedulas10 = cedulas1 = 0

print('=' * 30)
print(' ' * 10, 'BANCO CEV', ' ' * 30)
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))  # 50, 20, 10, 1
total = valor
ced = 50
totalCedulas = 0
condicao = False
while not condicao:
    if total >= ced:
        total -= ced
        totalCedulas += 1
        cedulas50 += 1
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} cédulas de R${ced}')
        if ced == 50:
            ced = 20
            cedulas20 += 1
        elif ced == 20:
            ced = 10
            cedulas10 += 1
        elif ced == 10:
            ced = 1
            cedulas1 += 1
        totalCedulas = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
'''
print(f'Total de {cedulas50:.0f} cédulas de R$50')
print(f'Total de {cedulas20:.0f} cédulas de R$20')
print(f'Total de {cedulas10:.0f} cédulas de R$10')
print(f'Total de {cedulas1:.0f} cédulas de R$1')
'''
