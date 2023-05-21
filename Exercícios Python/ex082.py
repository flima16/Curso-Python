valor = list()
impar = list()
par = list()
while True:
    valor.append(int(input('Digite um número: ')))
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp == 'S' or resp == 'N':
            break
        else:
                print('Opção Inválida!')
    if resp == 'N':
        break
for n in valor:
    if n % 2 != 0:
        impar.append(n)
    else:
        par.append(n)
print(f'Lista completa {valor}')
print(f'Lista com valores pares {par}')
print(f'Lista com valores impares {impar}')

