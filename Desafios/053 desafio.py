'''
Crie um Programa que leia uma frase qualquer
e diga se ela é um palíndromo, desconsiderando
os espaços.

Ex: APOS A SOPA
    A SACADA DA CASA
    A TORRE DA DERROTA
    O LOBO AMA O BOLO
    ANOTARAM A DATA DA MARATONA
'''

import re # retirar espaços no meio

print('-'*10, '\nPalíndromo', '\n', '-'*10)
frase = str(input('Digite uma frase: '))

fraseStrip = frase.strip()

fraseStrip = re.sub(r'\s+', '', fraseStrip)
#outra forma
# s = '  teste com espaços'
# s.replace(" ", "")
# 'testecomespaços'

print('Frase sem Espaços: {}'.format(fraseStrip))
tamanho1 = len(fraseStrip)
print('Tamanho da Frase: {}'.format(tamanho1))
print('Frase: {}'.format(fraseStrip))
frase = fraseStrip.upper()
print('Frase com Upper: {}'.format(frase))
tamanho2 = len(frase)

# dividir por 2 e encontrar a metade da frase com parte inteira
divisão = tamanho2 / 2

div = str(divisão) #passando para string
div = div.split('.') #quebrando em um vetor de split pelo ponto

divisãoParteInteira = int(div[0])
cont = 0
for c in range(0, tamanho2):
    if c < divisãoParteInteira:
        if frase[c] == frase[(tamanho2 - 1) - c]:
            cont += 1
if cont == divisãoParteInteira:
    print('Essa frase: \n{} \nÉ um palíndromo pois tem contador: {}'.format(frase, cont))
else:
    print('Essa frase: \n{} \nNão é palíndromo contador: {}'.format(frase, cont))

#resolução do Professor
newFrase = str(input('Digite uma frase: ')).strip().upper()
palavras = newFrase.split()
juntando = ''.join(palavras)
print('Você digitou a palavra {}'.format(juntando))
inverso = ''

for letra in range(len(juntando) - 1, -1, -1):
    inverso += juntando[letra]
print('O inverso de {} é {}!'.format(newFrase, inverso))
if inverso == juntando:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é palíndromo!')

# outra forma de inverter uma palavra é
inverso = juntando[::-1]
