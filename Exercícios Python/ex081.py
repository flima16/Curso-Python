valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp != 'S' and resp != 'N':
            print('Opção inválida!')
        else:
            break
    if resp == 'N':
        break
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse = True)
print(f'Os valores em ordem decrescente são {valores}')
print('O valor 5 faz parte da lista' if 5 in valores else 'O valor 5 não faz parte da lista')
