'''
Desenvolva um programa que leia o
nome, idade e sexo de quatro pessoas.
No final do programa, mostre:

- A média de idade do Grupo
- Qual é o nome do homem mais velho
- Quantas Mulheres têm menos de 20 anos.
'''

nome = ''
idade = 0
sexo = ''

totalIdades = 0
media = 0
oldMan = 0
nomeOldMan = ''
qtdMulheresMenores = 0

for dados in range(0, 4):
    print('------- {}° PESSOA -------'.format(dados + 1))
    nome = str(input('Digite o nome da Pessoa: ')).strip()
    idade = int(input('Digite a idade da Pessoa: '))
    sexo = str(input('Digite qual o Sexo da Pessoa: ')).strip()

    #media
    totalIdades += idade

    # oldMan
    if sexo == 'M' or sexo == 'Masculino' or sexo == 'MASCULINO':
        if idade > oldMan:
            oldMan = idade
            nomeOldMan = nome
    #qtdMulheres
    if sexo == 'F' or sexo == 'Feminino' or sexo == 'FEMININO':
        if idade < 20:
            qtdMulheresMenores += 1

media = totalIdades / 4
print('\nA média de Idades desse Grupo de 4 Pessoas é: {}'.format(media))
print('O nome do Homem mais velho é: {}'.format(nomeOldMan))
print('{} Mulher(es) têm menos de 20 anos de Idade'.format(qtdMulheresMenores))
