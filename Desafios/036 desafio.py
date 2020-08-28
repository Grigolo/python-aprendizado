'''
Escreva um programa para aprovar um empréstimo bancário
para a compra de uma casa. O programa vai perguntar
o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal. Sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será negado.
'''
valorCasa = float(input('Qual valor da Casa: '))
salarioComprador = float(input('Qual o salário do comprador: '))
pgtoQtdAnos = int(input('Quantos anos vai pagar a casa: '))

prestacoes = pgtoQtdAnos * 12

valorMensal = valorCasa / prestacoes

print('O valor da casa {} salario comprador {} Quantidade de Anos para pagar {} prestações {} '.format(valorCasa, salarioComprador, pgtoQtdAnos, prestacoes))

print('O valor mensal que será pago é {:.2f}'.format(valorMensal))

#calcular se valor excede 30% do salario
calculoSalario = salarioComprador * 0.3



if valorMensal > calculoSalario:
    print('Empréstimo Negado devido a mensalidade {} exceder 30% que é {}'.format(valorMensal, calculoSalario))
else:
    print('Emprestimo concedido, sua mensalidade é de {:.2f} e seu salario até 30% é {:.2f}'.format(valorMensal, calculoSalario))

