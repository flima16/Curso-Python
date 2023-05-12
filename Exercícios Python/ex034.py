sal = float(input('Salario: '))
if sal > 1250.00:
    novosal = sal + (sal * 0.1)
    print('O reajuste será de 10%')
else:
    novosal = sal + (sal * 0.15)
    print('o reajuste será de 15%')
print(f'O novo salario é {novosal}')
