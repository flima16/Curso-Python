def medida(l, c):
    return l * c
print(' Controle de Terrenos ')
print('-' * 15)

lar = float (input('LARGURA (m): '))
com = float (input('COMPRIMENTO (m): '))
print(f'A área de um terreno {lar}x{com} é de {medida(lar,com):.1f}m')
