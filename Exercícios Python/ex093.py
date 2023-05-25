jogador = dict()
lista = list()
jogador['nome'] = str(input('Nome do Jogador: ')).strip()
partida = int(input(f'Quantas partidas {jogador["nome"]}: '))
for c in range(0, partida):
    lista.append(int(input(f'Quantos gols na partida {c + 1}: ')))
jogador['gols'] = lista
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partida} partidas')
jogador['total'] = 0
for c in range(0, partida):
    jogador['total'] += jogador['gols'][c]
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
for c in range(0, partida):
    print(f'  =>Na partida {c + 1}, fez {jogador["gols"][c]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
