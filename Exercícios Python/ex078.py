valores = list()
posi1 = list()
posi2 = list()
for c in range(1,6):
    valores.append(int(input(f'Digite o {c}º valor: ')))
for c,v in enumerate(valores):
    if c == 0:
        maior = menor = v
        posi1 = posi2 = c
print(f'Você digitou os valores {valores}')
print(f'O maior valor fornecido foi {max(valores)} nas posições ', end = '')
for c,v in enumerate(valores):
    if v == max(valores):
        print(f'{c + 1}...', end = '')
print()
print(f'O menor valor fornecido foi {min(valores)} nas posições ', end = '')
for c,v in enumerate(valores):
    if v == min(valores):
        print(f'{c + 1}...', end = '')
