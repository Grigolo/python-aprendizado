'''
Crei um programa que leia o ano de nascimento de
sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantos já são maiores
'''

from datetime import date

anoAtual = date.today().year

print('.'*10, '\n', 'Maioridade', '\n', '.'*10)
contMaiores = 0
contMenores = 0

print('Ano Atual: {}'.format(anoAtual))

for maioridade in range(0, 7):
    anoNascimento = int(input('Digite o ano do seu Nascimento: '))

    if anoAtual - anoNascimento < 21:
        print('Vc ainda não atingiu a Maioridade')
        contMenores += 1
    elif anoAtual - anoNascimento >= 21:
        print('Vc está na categoria de Maioridade')
        contMaiores += 1
print('De sete Pessoas pesquisadas: {} são Menores de Idade'.format(contMenores))
print('De sete Pessoas Pesquisadas: {} estão na categoria Maioridade'.format(contMaiores))




