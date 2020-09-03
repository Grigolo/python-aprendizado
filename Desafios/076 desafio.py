'''
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, oraganizando os dados em forma tabular.
'''

listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10.90, 'Picanha', 39.50, 'Borracha', 2.00, 'Compasso', 4.20, 'Livro', 34.90)

print('-'*60)
print(f'{"Listagem de Preços":^60}')
print('-'*60)
cont = 0
inicio = 0

for pos in range(inicio, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)

# outra solução de um colega
print('Solução de Colega do Curso em Vídeo')

for i in listagem:
    if type(i) is str:
        print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:>5.2f}')
print('--'*20)




