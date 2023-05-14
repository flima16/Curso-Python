print('+=' * 13)
print(f'\033[1;32m{"Números Primos":^25}\033[m')
print('+=' * 13)
c1 = 0
n = int(input('Escolha um número: '))

for c in range(2, n + 1):
    if n % c == 0:
        c1 += 1
if c1 == 1:
    print(f'O número {n} é \033[32mPRIMO\033[m')
else:
    print(f'O número {n} \033[31mNão é PRIMO\033[m')