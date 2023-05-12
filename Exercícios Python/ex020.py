from random import shuffle
from typing import List

aluno1 = str(input('Nome do aluno: '))
aluno2 = str(input('Nome do aluno: '))
aluno3 = str(input('Nome do aluno: '))
aluno4 = str(input('Nome do aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print(f'A ordem de sequencia da apresentação será: {lista}')
