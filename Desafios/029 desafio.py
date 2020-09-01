'''
Escreva um programa que leia a velocidade de um carro

Se ele ultrapassar 80km/h , mostre um mensagem dizendo que ele foi multado.

A multa vai custar R$ 7,00 por cada km acima do limite
'''

distancia = float(input("Digite a velocidade do seu carro: "))

if distancia > 80:

    multa  = distancia - 80
    print("Você foi multado com essa velocidade {}".format(distancia))
    print("Multa: {:.1f}".format(multa * 7))
else:
    print("Você é um excelente motorista andando a {:.1f}! :)".format(distancia))

