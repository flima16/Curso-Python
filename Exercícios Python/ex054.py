from datetime import datetime
print('=' * 20)
print(f'{"Maioridade":-^20}')
print('=' * 20)
maiores = 0
menores = 0
for c in range(0,7):
    ano = int(input('Seu ano de nascimento: '))
    if datetime.today().year - ano < 21:
        menores += 1
    else:
        maiores += 1
print(f'Das 7 pessoas:')
print(f'\033[1;31m{menores}\033[m não atingiram a maioridade.')
print(f'\033[1;34m{maiores}\033[m atingiram a maioridade.')