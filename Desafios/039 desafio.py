'''
Faça um programa que leia o ano de nascimento
de um jovem e informa de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo de alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date

data_atual = date.today()

print('Data utual: {}'.format(data_atual))

data_nascimento = int(input('Digite sua data de nascimento: '))

print('Sua data de Nascimento: {}'.format(data_nascimento))
print('Ano atual do sistema: {}'.format(data_atual.year))

quantosAnos = data_atual.year - data_nascimento

if quantosAnos > 18:
    print('Já Passou o tempo de alistamento você tem {} anos de idade, e o alistamento é com 18 anos de idade, já passou {} anos do alistamento'.format(quantosAnos, (quantosAnos - 18)))

elif quantosAnos == 18:
    print('É hora de se alistar você tem {} anos de idade'.format(quantosAnos, (18 - quantosAnos)))

elif quantosAnos < 18:
    print('Ainda vai chegar a hora de se alistar você tem {} anos de idade e ainda faltam {} anos para o alistamento'.format(quantosAnos, (18 - quantosAnos)))





