'''
Crie um programa que leia os vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores
'''

condicao = False
media  = soma =  maior = cont = 0
menor  = 10000

while not condicao:
    num = int(input('Digite um número: '))
    soma += num
    if menor > num:
        menor = num
    if maior < num:
        maior = num
    cont += 1

    desejaContinuar = int(input('Deseja continuar a digitar escolha [0/1] 0 sair e 1 continuar: '))
    if desejaContinuar == 0:
        condicao = True
media = soma / cont
print('A média dos valores é: {}'.format(media))
print('O menor valor é {}, O maior valor é {}.'.format(menor, maior))

print(f'Teste de F string python 3.6 +. A média é {media:.2f}. ')

