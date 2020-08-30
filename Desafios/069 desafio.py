'''
Crie um programa que leia a idade e sexo
de várias pessoas. A cada pessoa cadastrada o programa deverá
perguntar se o usuário quer ou não continuar .
No final, mostre:

A) quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos
'''
mulheresMenores20 = homens = maiores18 = 0


while True:

    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
         sexo = str(input('Digite o sexo da Pessoa [M/F]: ')).strip().upper()[0]

    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheresMenores20 += 1

    if idade > 18:
        maiores18 += 1

    opcao = ' '

    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if opcao == 'N':
        break

print('='*10, 'FIM DO PROGRAMA', '='*10)
print(f'Total de Pessoas com mais de 18 anos: {maiores18}')
print(f'Ao todo temos {homens}  homens cadastrados.')
print(f'E temos {mulheresMenores20} mulheres com menos de 20 anos.')


