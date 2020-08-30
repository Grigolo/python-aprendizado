'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles
(desconsiderando o flog condição de parada)
'''


condicao = False
soma  = 0
cont  = 0
while not condicao:
    num = int(input('Digite um número: '))
    if num == 999:
        condicao = True
    else:
        soma += num
        cont += 1
print('O total de Números digitados foram: {}'.format(cont))
print('A soma total dos número é: {}'.format(soma))
