c = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n != 999:
        c += 1
        soma += n
    else:
        break
print(f'A quantidade de valores fornecidos foi {c}')
print(f'A soma dos valores fornecidos foi {soma}')
