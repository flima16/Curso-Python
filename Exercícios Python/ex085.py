valor = list()
par = list()
impar = list()
juncao = list()
for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
par.sort()
impar.sort()
valor.append(par[:])
valor.append(impar[:])
juncao.append(valor[:])
print('-=' * 20)
print(f'Os valores pares digitados foram: {juncao[0][0]}')
print(f'Os valores ímpares digitados foram: {juncao[0][1]}')