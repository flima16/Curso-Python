from random import randint
print('=-' * 40)
print(f'{"VAMOS JOGAR PAR OU ÍMPAR"}')
print('=-' * 40)
flag = True
flag1 = True
result = 0
c = 0
while True:
    maq = randint(0, 10)
    n = int(input('Diga um valor: '))
    while flag == True:
       esc = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()
       if esc == 'P' or esc == 'I':
            flag = False
       else:
            print('Opção Inválida!')
    flag = True
    result = (n + maq) % 2
    print('-' * 40)
    print(f'Você jogou {n} e o computador {maq}. Total de {n + maq} ', end = '')
    if result == 0:
       print('DEU PAR')
       if  esc == 'P':
           c += 1
       else:
           flag1 = False
    else:
        print('DEU ÍMPAR')
        if esc == 'I':
            c += 1
        else:
            flag1 = False
    print('-' * 40)
    if flag1 == True:
        print('Você VENCEU!\nVamos jogar novamente...')
    else:
        print('Você PERDEU!')
        break
print('=-' * 40)
print(f'GAME OVER! Você venceu {c} vezes.')
