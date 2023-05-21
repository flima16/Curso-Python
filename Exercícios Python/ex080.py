from typing import List

valores = list()

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    valores.append(n)
    for pos, v in enumerate(valores):
        if n < v:
            valores.insert(pos, n)
            valores.pop()
            break
    for pos, v in enumerate(valores):
        if n == v and pos == len(valores) - 1:
            print('Adicionado ao final da lista...')
            break
        elif n == v:
            print(f'Adicionado na posição {pos} da lista...')
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')