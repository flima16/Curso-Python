print('=' * 20)
print(f'{"Tabuada":^20}')
print('=' * 20)
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n >= 0:
        print('-' * 40)
        for c in range(1, 11):
            print(f'\033[1;34m{n} x {c}\033[m = \033[1;31m{n * c}\033[m')
        print('-' * 40)
    else:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')