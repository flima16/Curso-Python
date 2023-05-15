print('=+' * 10)
print(f'{"PALÍNDROMO":=^20}')
print('=+' * 10)
frase = str(input('Digite uma frase: ')).strip().upper()
frase1 = frase[::-1]
frase = frase.split()
frase = 'x'.join(frase)
frase1 = frase1.split()
frase1 = 'x'.join(frase1)
print(frase1)
cont = 0
c1 = 0
c2 = 0
p = len(frase) - len(frase.split())
for c in range(0, len(frase)):
    if c1 < len(frase) or c2 < len(frase):
        if frase[c1] == 'x' and frase1[c2] == 'x':
              c1 += 1
              c2 += 1
        elif frase[c1] == 'x':
            c1 += 1
            if frase[c1] == frase1[c2]:
                cont += 1
                c1 += 1
                c2 += 1
        elif frase1[c2] == 'x':
            c2 += 1
            if frase[c1] == frase1[c2]:
                cont += 1
                c1 += 1
                c2 += 1
        elif frase[c1] == frase1[c2]:
            cont += 1
            c1 += 1
            c2 += 1
        else:
            break
    else:
        break
if c1  == len(frase):
    print('\033[1;34mA frase forma um PALÍNDROMO\033[m')
else:
    print('\033[1;31mA frase não forma um PALÍNDROMO\033[m')