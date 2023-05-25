from random import randint
from time import sleep
c = 1
posicao = dict()
copia = list()
jogador = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6)}
print('Valores sorteados: ')
for k,v in jogador.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ordenado = {k: v for k,v in sorted(jogador.items(), key = lambda item: item[1], reverse = True)}
print('Ranking dos jogadores:')
for k,v in ordenado.items():
    print(f'{c}º lugar: {k} com {v}')
