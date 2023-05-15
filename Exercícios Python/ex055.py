maior = 0
menor = 1000
for c in range(0,5):
    peso = int(input('Seu peso: '))
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso
print(f'O maior peso fornecido foi {maior}')
print(f'O menor peso fornecido foi {menor}')