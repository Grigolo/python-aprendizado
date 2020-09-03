'''
Crie um programa que tenha uma tupla
com várias palavras (não usar acentos)
Depois disso você deve mostrar, para cada palavra
quais são as suas vogais.

'''

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
vogais = ''
p = ''
for pos in range(0, len(palavras)):
    for p in palavras[pos]:
        if 'a' in p:
            vogais += 'a '
        if 'e' in p:
            vogais += 'e '
        if 'i' in p:
            vogais += 'i '
        if 'o' in p:
            vogais += 'o '
        if 'u' in p:
            vogais += 'u '

    print(f'Na Palavra {palavras[pos].upper()} temos {vogais}')
    vogais =''
# resolução do Professor
print(f'=-'*30)
print(f'{"Resolução do Professor":^30}')
print(f'=-'*30)
for pa in palavras:
    print(f'\nNa palavra {pa.upper()} temos ', end='')
    for letra in pa:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
