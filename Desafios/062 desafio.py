'''
Melhore o desafio 61.
Perguntando para o usuário se ele quer
mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar.
0 termos
'''

primeiroTermo = int(input('Digite qual o Primeiro Termo da PA: '))
razao = int(input('Digite qual a razão da PA: '))

print('\nWhile Fersontec')
cont = 1
lista = 0
terminar = 10

while cont <= terminar:
    if cont > 1:
        lista += razao
        print(' {} '.format(lista), end='->')
    else:
        lista += primeiroTermo

        print(' {} '.format(lista), end='->')
    cont += 1

    if cont == terminar+1:
        maisTermos = int(input('\nDigite 0 para sair. ou Quantos termos vc quer que se exibido a mais: '))
        if maisTermos > 0:
            terminar += maisTermos

print('Progressão Finalizada com {} termos mostrados'.format(cont - 1))
