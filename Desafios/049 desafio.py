'''
Refaça o desafio 009 da tabuada. Mostrando a tabuada
de um número que o usuário escolher. só que agora
utilizando um laço for.
'''

num = int(input('Digite o número para o sistema realizar a tabuada? '))

print('{} Bem Vindos a Tabuada '.format('-'*10))
for tabuada in range(0, 11):

    total = 0
    total = tabuada * num
    print('{} X {} = {}'.format(tabuada, num, total))
print('Fim Tabuada')
