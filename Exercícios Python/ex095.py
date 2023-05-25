jogador = dict()
lista = list()
lista1 = list()
copia = list()
print('-' * 30)
while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        lista.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = lista
    jogador['total'] = 0
    lista.clear()
    for c in range(0, partidas):
        jogador['total'] += jogador['gols'][c]
    lista1.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp == 'S' or resp == 'N':
            break
        else:
            print('Opção Inválida!')
    if resp == 'N':
        break

print('-=' * 30)
print(f'{"cod":<4}{"nome":<6}{"gols":>8}{"total":>10}')
print('-' * 30)
for c in range(0, len(lista1)):
    print(f'{c + 1}  {(lista1[c]["nome"]):>4}  {(lista1[c]["gols"])}  {lista1[c]["total"]}')
print('-' * 30)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para finalizar) '))
    if busca == 999:
        break
    if busca <= 0 or busca > len(lista1):
        print('Não existe jogador com esse código')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista1[busca - 1]["nome"]}')
        busca -= 1
        for i,g in enumerate(lista1[busca]['gols']):
            print(f'     No jogo {i + 1} fez {g}')
print('-' * 30)
print('<<  VOLTE SEMPRE >>')



