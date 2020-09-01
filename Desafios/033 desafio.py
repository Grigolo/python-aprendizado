'''
Faça um programa que leia três números e mostre
qual é o maior e qual é o menor.
'''

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

menor = n1
#verificar o menor
if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
# verificar o maior
if n2 < n1 and n2 < n3:
    maior = n2

if n3 < n1 and n3 < n2:
    menor = n3

print("Números digitados {}, {}, {} \n O maior número é: {} O menor número é: {}".format(n1, n2, n3, maior, menor))
