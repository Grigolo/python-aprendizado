'''
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro de Futebol.
Na ordem de classificação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time da Chapecoense
'''

times = ('Atlético MG', 'Athético PR', 'Internacional', 'Grêmio', 'Atlético GO', 'Vasco da Gama', 'Bahia', 'São Paulo', 'Sport Recife', 'Flamengo', 'Palmeiras', 'Bragantino SP', 'Ceará SC', 'Botafogo', 'Corinthians', 'Goiás', 'Fluminense', 'Santos', 'Fortaleza', 'Coritiba')
print('=-'*30)
print('Lista de Times do Brasileirão')
print(times)
print('=-'*30)

print(f'Os 5 primeiros são: {times[0:5]}')
print('=-'*30)
print(f'Os 4 Últimos são: {times[16:21]}') # times[-4:] do menos -4 até o último

print('=-'*30)
print(f'Times em ordem alfabético: {sorted(times)}')
print('=-'*30)

print(f'Resolução Professor: O Fluminense está na {times.index("Fluminense") + 1}° posição.')
for pos, nome in enumerate(times):
    if nome == 'Fluminense':
        print(f'O Fluminense está na {pos + 1}º posição')
        break


