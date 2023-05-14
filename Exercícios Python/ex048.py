print('Vamos Calcular Múltiplos Ímpares de 3')
soma = 0
p = 30
for c in range(1, p + 1):
    if c % 2 == 1:
        if c % 3 == 0:
            soma += c
print('A soma de todos os múltiplos ímpares de 3', end = '')
print(f' \nno intervalo de 1 a {p} é igual a \033[1;31m{soma}\033[m ')