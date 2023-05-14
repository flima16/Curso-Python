print(f'{"Tabuada":=^20}')
n = int(input('Escolha o número: '))
for c in range(1, 11):
    print(f'\033[1;34m{n} x {c}\033[m = \033[1;32m{n * c}\033[m')