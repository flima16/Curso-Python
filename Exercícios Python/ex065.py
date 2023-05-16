flag = 'S'
c = 0
media = 0
maior = 0
menor = 1000000
while flag in 'S':
    n = int(input('Digite um número: '))
    c += 1
    media += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    flag = str(input('Quer continuar? [S/N]: ')).strip().upper()
print(f'Você digitou {c} números e a média foi {media / c:.2f}')
print(f' O maior valor foi {maior} e o menor foi {menor}')