'''
Faça um programa que calcule a soma entre
todos os números ímpares que são múltiplos
de três e que se encontram no intervalo de
1  a 500.
'''
soma  = 0
cont = 0
for imparesMultiplosTres in range(1, 501, 2):
    if imparesMultiplosTres % 3 == 0:
        cont += 1
        soma += imparesMultiplosTres
        print('Esse número {} é divisível por 3.'.format(imparesMultiplosTres))
print('Total de números somadas foram {}. A soma total é {}.'.format( cont, soma))
