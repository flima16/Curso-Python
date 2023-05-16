print(f'{"FIBONACCI":=^30}')
n = int(input('Quantos termos: '))
c = 0
acm = 1
ant = 0
soma = 0
while c < n:
    if c == 0 or c == 1:
        print(f'{c} → ', end = '')
    else:
        soma = acm + ant
        ant = acm
        acm = soma
        print(f'{soma} → ', end = '')

    c += 1
print('FIM')