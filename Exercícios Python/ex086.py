matriz = list()
copia = list()
for c in range(0,3):
    for c1 in range(0,3):
        copia.append(int(input(f'Digite um valor para [{c+1},{c1 + 1}]: ')))
    matriz.append(copia[:])
    copia.clear()
print('-=' * 20)
for c in range(0,3):
    for c1 in range(0,3):
        print(f'[ {matriz[c][c1]:5} ] ', end = '')
    print()
