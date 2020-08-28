'''
Crie um programa que faça o computador
jogar jokenpô com você.

- Pedra
- Pape
- Tesoura
'''
from random import randint
from time import sleep
itens = ('Papel', 'Pedra', 'Tesoura')
jogadorUser = int(input('''Bem vindo ao Jogo Jokenpô:
[ 0 ] Papel
[ 1 ] Pedra
[ 2 ] Tesoura
Qual opção? '''))

print('Escolha do Jogador User: {}'.format(jogadorUser))
escolhaSistema = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-=' * 14)
print('Sistema Jogou: {}'.format(itens[escolhaSistema]))
if jogadorUser == 0 or jogadorUser == 1 or jogadorUser == 2:
    print('Jogador jogou: {}'.format(itens[jogadorUser]))
print('-=' *14)

if jogadorUser == escolhaSistema:
    print('O jogo deu empate os dois escolheram {}'.format(itens[escolhaSistema]))
elif jogadorUser == 0: #papel
    if escolhaSistema == 1: #pedra
        print('Parabéns o jogador User ganhou do sistema. Vc escolheu {} e o sistema escolheu {}. Papel embrulha a pedra'.format(itens[jogadorUser], itens[escolhaSistema]))
    elif escolhaSistema == 2: #tesoura
        print('Vc perdeu o sistema ganhou, sua escolha {} e o sistema {}. Tesoura corta o papel '.format(itens[jogadorUser], itens[escolhaSistema]))
elif jogadorUser == 1: # pedra
    if escolhaSistema == 0: #papel
        print('O sistema ganhou. o sistema jogou {} e sua escolha {}. '.format(itens[escolhaSistema], itens[jogadorUser]))
    elif escolhaSistema == 2: #tesoura
        print('Parabéns vc ganhou sua escolha {} sistema {}.'.format(itens[jogadorUser], itens[escolhaSistema]))
elif jogadorUser == 2: #tesoura
    if escolhaSistema == 0: #papel
        print('Vc ganhou papel corta a tesoura')
    elif escolhaSistema == 1: #pedra
        print('Vc perdeu a pedra quebra a tesoura')
else:
    print('Jogada Inválida, tente novamente!!!')
