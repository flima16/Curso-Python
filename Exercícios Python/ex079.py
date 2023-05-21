valores = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp == 'N' or resp == 'S':
            break
        else:
            print('Opção Inválida!')
    if resp == 'N':
        break
print('-=' * 20)
valores.sort()
print(f'Você digitou os valores {valores}')


