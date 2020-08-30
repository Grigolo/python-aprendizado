'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai acontecer.
No final, mostre:

A) Qual é o total de gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
'''

totalCompra = produtosAcima1000 = 0

nomeProdutoBarato = ''
precoProdutoBarato = 100000

while True:
    print('-'*30)
    print('CADASTRO DE PRODUTOS')
    print('-'*30)

    nomeProd = str(input('Digite o nome do Produto: ')).strip().upper()
    precoProd = float(input('Digite o Preço do Produto: '))

    totalCompra += precoProd
    if precoProd > 1000:
        produtosAcima1000 += 1
    if precoProd < precoProdutoBarato:
        precoProdutoBarato = precoProd
        nomeProdutoBarato = nomeProd

    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if opção == 'N':
        break
print('FIM DO PROGRAMA')
print(f'Total de Gasto na compra: {totalCompra}')
print(f'Foram cadastrados \033[1;91m {produtosAcima1000} \033[m acima de R$ 1000')
print(f'O nome do Produto mais barato é {nomeProdutoBarato} que custa R${precoProdutoBarato}')
