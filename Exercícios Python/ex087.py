matriz = list()
par = coluna = 0
copia = list()
for c in range(0,3):
    for c1 in range(0,3):
        copia.append(int(input(f'Digite um valor para [{c + 1},{c1 + 1}]: ')))
    matriz.append(copia[:])
    copia.clear()
for c in range(0,3):
    for c1 in range(0,3):
       if matriz[c][c1] % 2 == 0:
           par += matriz[c][c1]
       if c1 == 2:
           coluna += matriz[c][c1]
       if c == 1:
           copia.append(matriz[c][c1])
print('-=' * 30)
for c in range(0,3):
    for c1 in range(0,3):
        print(f'[ {matriz[c][c1]} ] ', end = '')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {coluna}')
print(f'O maior valor da segunda linha é {max(copia)}')
