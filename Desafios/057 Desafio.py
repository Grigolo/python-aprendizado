'''
Faça um programa que leia o sexo de uma pessoa.
Mas só aceite os valores 'M' ou 'F'.
Caso esteja errado peça a digitação até ter um valor correto.
'''

cont = 0
sexo = ''
sexo = str(input('Digite seu sexo no Formato [M/F]: ')).strip().upper()[0]

print('Sexo digitado inicialmente: {}'.format(sexo))
if sexo == 'M' or sexo == 'F':
    cont = 1
else:
    while cont == 0:
        print('Sexo no formato errado.')
        sexo = str(input('Digite novamente seu sexo no Formato [M/F]: ')).strip().upper()[0]
        if sexo == 'M' or sexo == 'F':
            cont = 1

print('Fim da execução vc digite o sexo: {}'.format(sexo))


# Resolução do Professor

sexoUser = str(input('Digite o sexo do User: ')).strip().upper()[0]
while sexoUser not in 'MF':
    sexoUser = str(input('Dados inválidos. Por favor digite seu Sexo: ')).strip().upper()[0]

print('Está certo o User digitou o SEXO {}'.format(sexoUser))



