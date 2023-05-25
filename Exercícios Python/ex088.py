from random import randint
mega = list()
palpite = list()
copia = list()
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)

resp = int(input('Quantos jogos você quer que eu palpite? '))
print('-=' * 3, f' SORTEANDO {resp} JOGOS ', '-=' * 3)
for c in range(0, resp):
    for c1 in range(0,6):
       while True:
          n = randint(1,60)
          if n not in palpite:
              palpite.append(n)
              break
    copia.append(palpite[:])
    palpite.clear()
mega.append(copia[:])

for c in range(0,4):
    print(f'Jogo {c + 1}: {mega[0][c]}')
print('-=' * 5, f' BOA SORTE ', '-=' * 5)



