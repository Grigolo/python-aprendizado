'''
Faça um programa que leia um número
qualquer e mostre o seu fatorial.

Ex: 5! = 5*4*3*2*1 = 120
'''
print('.'*10, 'Fatorial', '.'*10)
num = int(input('Digite um número: '))

fatorial = 1
calculo = num
while calculo > 1:
    #print(fatorial, '*', calculo)
    fatorial *= calculo
    calculo = calculo - 1

print('O fatorial de {} é: {}'.format(num, fatorial))

# resolução do professor
c = num
cal = 1
print('Calculando {}! = '.format(c), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    cal *= c
    c -= 1
print('{}'.format(cal))


