print('Os números pares no intervalo de 1 a 50 é')
c1 = 0
for c in range(1,51):
    if c % 2 == 0:
        print(f'{c}\t', end = '')
        c1 += 1
        if c1 % 5 == 0:
            print('\n')