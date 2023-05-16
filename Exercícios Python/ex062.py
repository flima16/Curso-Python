print('=' * 30)
print(f'{"Progressão Aritmética":-^30}')
print('=' * 30)
termo = int(input('Qual é o primeiro termo: '))
razao = int(input('Qual a razao: '))
c = 10
c1 = 0
cont = 0
while c != 0:
    while c1 != c:
        cont += 1
        print(f'{termo} → ', end = '')
        termo += razao
        c1 += 1
    print('Pausa')
    c = int(input('Quantos termos quer mostrar? '))
    c1 = 0
print(f'Progressão finalizada com {cont} termos mostradas.')