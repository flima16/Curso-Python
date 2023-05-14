print('+=' * 20)
print(f'\033[31m{"Progressão Aritmética":-^40}\033[m')
print('+=' * 20)
termo = int(input('Qual o primeiro termo da PA: '))
razao = int(input('Qual a razão: '))
print('Os dez primeiros termos dessa progressão são:')
for c in range(0, 10):
    print(f'{termo}\t', end = '')
    termo += razao

