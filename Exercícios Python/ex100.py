from random import randint

def sorteia():
    return randint(1,10)

def somaPar(num):
    soma = 0
    for c in num:
        if c % 2 == 0:
            soma += c
    return soma

def mensagem(num):
    for c in num:
        print(c, end = ' ')

numeros = list()

for c in range(0, 5):
    numeros.append(sorteia())
print(f'Sorteando 5 valores da lista:', end = ' ')
mensagem(numeros)
print('PRONTO!')
print(f'Somando os valores pares de {numeros}, temos {somaPar(numeros)} ')