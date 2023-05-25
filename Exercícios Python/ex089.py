nota = list()
cadastro = list()
copia = list()
media = list()
aluno = list()
while True:
    aluno.append(str(input('Nome: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    media = (nota[0] + nota[1]) / 2
    aluno.append(nota[:])
    aluno.append(media)
    copia.append(aluno[:])
    aluno.clear()
    nota.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp == 'N' or resp == 'S':
            break
    if resp == 'N':
        break
cadastro.append(copia[:])
print(cadastro)
print('-=' * 40)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 20)
for c in cadastro:
    for c1 in range(0,len(c)):
        print(f'{c1 + 1:<4}{c[c1][0]:<10}{c[c1][2]:>8.1f}')
while True:
    print('-' * 20)
    resp = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if resp == 999:
        break
    for c in cadastro:
        print(f'Notas de {c[resp - 1][0]} são {c[resp - 1][1]}')

print('FINALIZANDO...')
print('-=' * 5, f'{" FIM DO PROGRAMA "}', '-=' * 5)