from random import randint
from time import sleep
nome = 'Advinhar'
print(f'{nome:=^20}')
num = int(input("""Escolha um valor de 0 a 5 
e veja se você advinha o número sorteado: """))
rand = randint(0,5)
print('Processando...')
sleep(2)
print(f'O número sorteado foi {rand}')
print('Você acertou' if rand == num else 'Você errou')
print('------FIM------')