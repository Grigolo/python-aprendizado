'''
Elabore um programa que calcule o valor a ser pago por um produto
considerando o seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

preçoProduto = float(input('Digite o valor do produto: '))

condiçãoPagamento = int(input('''Escolha qual a forma de Pagamento:
[ 1 ] À vista dinheiro ou Cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a Opção? '''))

if condiçãoPagamento == 1:
    total = preçoProduto - ((preçoProduto * 10) / 100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preçoProduto, total))
elif condiçãoPagamento == 2:
    total = preçoProduto - ((preçoProduto * 5 ) /100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preçoProduto, total))
elif condiçãoPagamento == 3:
    total = preçoProduto
    parcela = total / 2
    print('Sua compra total de R$ {:.2f} será parcelada em 2x de R$ {:.2f} SEM Juros'.format(preçoProduto, parcela))
elif condiçãoPagamento == 4:
    total = preçoProduto + ((preçoProduto * 20) /100)
    totalParcelas = int(input('Quantas parcelas? '))
    parcela = total / totalParcelas
    print('Sua compra total de R$ {:.2f}, será parcelada em {}x de R$ {:.2f} com Juros'.format(preçoProduto, totalParcelas, parcela))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preçoProduto, total))
else:
    print('Condição de pagamento inválida tente novamente')

