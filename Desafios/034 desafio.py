'''
Escreva um programa que pergunte o salário de
um funcionário e calcule o valor do seu aumento

-> Para salários superiores a R$ 1250,00 calcule aumento de 10%

-> Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input("Digite o seu salário: "))

s = salario

if salario > 1250:
    salario = salario + (salario * 10) / 100
    print("Salário antigo {}, com aumento ficou salário de {}.".format(s, salario))
else:
    print("Salário antigo {} novo salário após aumento {}".format(s, salario + (salario * 15)/100))
