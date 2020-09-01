'''
Desenvolva um programa que leia o comprimento de três retas e diga
ao usuário se elas podem ou não formar um triângulo
'''


'''
regras para criar triangulo

(b - c) < a < (b + c)
(a - c) < b < (a + c)
(a - b) < c < (a + b)
'''
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and  (a - b) < c < (a + b):
    print("Esses valores formam um triângulo :)")
else:
    print("Esses valores não formam um triângulo tente novamente :(")

# ************* Maneira de resolver do Professsor
if a < b + c and b < a + c and c < a + b:
    print("Valores formam triângulo Guanabara")

else:
    print("Deu ruim digite novamente")
