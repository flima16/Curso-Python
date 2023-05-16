print('=' * 30)
print(f'{"Progressão Aritmética":-^30}')
print('=' * 30)

c = 1
termo = int(input('Qual é o primeiro termo: '))
razao = int(input('Qual a razao: '))
while c < 11:
    print(f'{termo} ', end = '')
    termo += razao
    c += 1