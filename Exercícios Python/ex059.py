print('=' * 20)
print(f'{"Calculadora":-^20}')
print('=' * 20)
flag = 0
flag1 = 0
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor:'))
while flag == 0:
    while flag1 == 0:
        print('-' * 10)
        print(f'{"Menu":^10}')
        print('=' * 10)
        n3 = int(input('[ 1 ]Somar\n[ 2 ]Multiplicar\n[ 3 ]Maior\n[ 4 ]Novos Números\n[ 5 ]Sair\nOpção: '))
        if n3 <= 5 and n3 > 0:
            flag1 += 1
        else:
            print('Opçao Invalida!')
    if n3 == 5:
        flag += 1
    elif n3 == 1:
        print(f'\033[1;34m{n1} + {n2}\033[m = \033[1;31m{n1 + n2}\033[m')
        flag1 = 0
    elif n3 == 2:
        print(f'\033[1;34m{n1} x {n2}\033[m = \033[1;31m{n1 * n2}\033[m')
        flag1 = 0
    elif n3 == 3:
        if n1 > n2:
            print(f'O maior valor entre {n1} e {n2} é {n1}')
            flag1 = 0
        else:
            print(f'O maior valor entre {n1} e {n2} é {n2}')
            flag1 = 0
    else:
        print(('Informe Novamente'))
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor:'))
        flag1 = 0
    print('-=' * 20)
