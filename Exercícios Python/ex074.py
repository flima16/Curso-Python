from random import randint
def sorteio():
    return randint(0, 10)
tupla = (sorteio(), sorteio(), sorteio(), sorteio(),sorteio())

print(f'Os valores sorteado foram:\t ',end = '')
for c in range(0,5):
    print(f'{tupla[c]}\t', end = '')

print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')