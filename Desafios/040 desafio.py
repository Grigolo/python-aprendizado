'''
Crie um prograama que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: Reprovado

- Média entre 5.0 e 6.9: Reprovação

- Média 7 ou superior: Aprovado
'''

primeiraNota = float(input('Digite a primeira nota: '))
segundaNota = float(input('Digite a segunda nota: '))

media = (primeiraNota + segundaNota) / 2

print('Suas notas foram: Na primeira {:.1f}, na segunda {:.1f}'.format(primeiraNota, segundaNota))

print('Sua média é: {:.1f}'.format(media))

if media < 5:
    print('Suas notas foram: {}  e  {} com isso Você tem a média {}, com isso você está reprovado.'.format(primeiraNota, segundaNota, media))

elif 7 > media >= 5:
    print('Suas notas foram {} e {} com isso Sua média é {}, você está em recuperação.'.format( primeiraNota, segundaNota, media))

elif media >= 7:
    print('Suas Notas foram {} e {} com isso Sua média é: {}, Parabéns você está aprovado.'.format(primeiraNota, segundaNota,media))

