print('=' * 20)
print(f'{"BANCO CEV":^20}')
print('=' * 20)
valor = int(input('Que valor você quer sacar? R$'))
c50 = c20 = c10 = c1 = 0
while valor != 0:
    if valor >= 50:
        valor -= 50
        c50 += 1
    elif valor < 50 and valor >= 20:
        valor -= 20
        c20 += 1
    elif valor < 20 and valor >= 10:
        valor -= 10
        c10 += 1
    else:
        valor -= 1
        c1 += 1
print(f'Total de {c50} cédulas de R$50')
print(f'Total de {c20} cédulas de R$20')
print(f'Total de {c10} cédulas de R$10')
print(f'Total de {c1} cédulas de R$1')
print('=' * 20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
