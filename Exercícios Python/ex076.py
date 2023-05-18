print('-' * 41)
print(f'{"LISTAGEM DE PREÇOS":^41}')
print('-' * 41)

tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for c in range(0,18):
    if c % 2 == 0:
        print(f'{tupla[c]:.<30}', end = '')
    else:
        print(f'R$  {tupla[c]:.2f}', end = '')
        print('\t')
print('-' * 41)