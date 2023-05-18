brasileirao = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atletico', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
for c in range(0, 5):
    print('=-' * 20)
    if c == 0:
        print(f'Lista de times do Brasileirão: {brasileirao}')
    elif c == 1:
        print(f'5 primeiros são: {brasileirao[0:5]}')
    elif c == 2:
        print(f'4 últimos são: {brasileirao[-4:]}')
    elif c == 3:
        print(f'Times em ordem alfabética: {sorted(brasileirao)}')
    else:
        print(f'Chapecoense está na {brasileirao.index("Chapecoense") + 1}ª posição')
