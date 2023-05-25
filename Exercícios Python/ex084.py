pesagem = list()
dados = list()
peso = list()
c = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pesagem.append(dados[:])
    c += 1
    dados.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp == 'N' or resp == 'S':
            break
        else:
            print('Opção Incorreta!')
    if resp == 'N':
        break
for v in pesagem:
    peso.append(v[1])
print('-=' * 30)
print(f'Ao todo, você cadastrou {c} pessoas.')
print(f'O maior peso foi de {max(peso):.1f}Kg. Peso de ', end = '')
for v in pesagem:
    if max(peso) == v[1]:
        print(f'{v[0]} ', end = '')
print()
print(f'O menor peso foi de {min(peso):.1f}Kg. Peso de ', end = '')
for v in pesagem:
    if min(peso) == v[1]:
        print(f'{v[0]} ', end = '')


