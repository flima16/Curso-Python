from random import randint
flag = 0
c = 0
print('=' * 20)
print(f'{"Advinhação":-^20}')
print('=' * 20)
maq = randint(0, 10)
print('Advinhe o número que estou pensando de 0 a 10')
while flag == 0:
    num = int(input('Qual seu palpite: '))
    c += 1
    if num != maq:
        if num < maq:
            print('Mais. Tente Novamente!')
        else:
            print('Menos. Tente Novamente!')
    else:
        print('\033[1;34mVocê Acertou\033[m\nParabéns!')
        flag += 1
print(f'Você precisou de {c} palpites')
