'''
A confederação nacional de natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre a sua categoria
de acordo com a idade:

 - Até 9 anos: Mirin
 - Até 14 anos:  Infantil
 - Até 19 anos: Junior
 - Até 20 anos: Sênior
 - Acima: Master
'''
from datetime import date
data_atual = date.today()

anoNascimento = int(input('Digite seu ano de Nascimento: '))

qtdAnosIdade = data_atual.year - anoNascimento

print('Você tem {} anos de idade.'.format(qtdAnosIdade))

if qtdAnosIdade <= 9:
    print('Você tem {} anos de Idade. Sua categoria é Mirin'.format(qtdAnosIdade))

elif qtdAnosIdade <= 14:
    print('Você tem {} de idade. Sua categoria é Infantil.'.format(qtdAnosIdade))

elif qtdAnosIdade <= 19:
    print('Sua idade é {} anos. Sua categoria é Junior.'.format(qtdAnosIdade))

elif qtdAnosIdade <= 20:
    print('Sua idade é {} anos, sua categoria é Sênior'.format(qtdAnosIdade))

elif qtdAnosIdade > 20:
    print('Sua idade é {} anos, sua categoria é Master'.format(qtdAnosIdade))
