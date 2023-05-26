def maior(m):
    for c, v in enumerate(m):
        if c == 0:
            max = v
        else:
            if v > max:
                max = v
    return max

def mensagem(num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    texto(num)
    print(f'O maior valor informado foi {maior(num)}')

def texto(num):
    for c in num:
        print(c, end = ' ')
    print(f'Foram informados {len(num)} valores ao todo.')

cont = list()
while True:
    cont.append(int(input('Valor: ')))
    while True:
        resp = str(input('Deseja forncer mais um valor? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
        else:
            print('Opção Inválida. Somente S-Sim ou N-não')
    if resp == 'N':
        break
mensagem(cont)