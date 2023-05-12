distancia = int(input('Distancia da Viagem (km): '))
if distancia <= 200:
    print(f'O preço da passagem custará R${distancia * 0.5:.2f}')
else:
    print(f'O preço da passagem custará R${distancia * 0.45:.2f}')