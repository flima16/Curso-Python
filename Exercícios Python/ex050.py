soma = 0
for c in range(1, 7):
    n = int(input(f'Digite {c}º número: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos números pares fornecidos é igual a {soma}')