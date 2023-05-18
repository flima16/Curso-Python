tupla = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um númeor: ')), int(input('Digite o último número: ')))
c1 = 0
for c in range(0,4):
    if tupla[c] % 2 == 0:
        c1 += 1
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição')
print(f'Os valores pares digitados foram {c1}')