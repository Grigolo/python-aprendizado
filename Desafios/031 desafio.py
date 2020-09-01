'''
Desenvolva um que pergunta a distância de uma viagem em KM.
Calcule o preço da passagem. Cobrando R$ 0,50 por KM
para viagens de até 200km e R$ 0,45 para viagens mais longas.
'''

distancia = float(input("Digite a distância que você tem que percorrer: "))

precoCurto = 0.50

precoLongo = 0.45

if distancia <= 200:
    print("Você vai percorrer {} km e vai ter que pagar R$ {}".format(distancia, precoCurto * distancia))

elif distancia >200:
    print("Você vai percorrer {} km longo caminho e vai pagar R$ {} de passagem.".format(distancia, precoLongo * distancia))
