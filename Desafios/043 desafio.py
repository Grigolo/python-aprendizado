'''
Desenvolva uma lógica que leia o pessoa e a altura de uma pessoa.
Calcule seu IMC e mostre seu status, de acordo com a tabela abaixa:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

peso  = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

print('Seu peso é {}, altura: {}, seu IMC é {:.2f}'.format(peso, altura, imc))
if imc < 18.5:
    print('Vc está abaixo do peso')
elif 18.5 < imc < 25:
    print('Vc está com o peso Ideal')
elif 25 <= imc < 30:
    print('Vc está com sobrepeso')
elif 30 <= imc < 40:
    print('Vc está com obesidade')
else:
    print('Vc está com obesidade mórbida')
