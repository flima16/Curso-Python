c = 0
soma = 0
flag = int(input('Digite um número [999 para parar]: '))
while flag != 999:
    c += 1
    soma += flag
    flag = int(input('Digite um número: '))
print(f'A soma dos valores lidos é {soma}')
print(f'Foram fornecidos {c} valores')