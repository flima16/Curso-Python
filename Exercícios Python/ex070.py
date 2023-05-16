print('-' * 30)
print(f'{"LOJA SUPER BARATÃO":^30}')
print('-' * 30)
compra = cont = preco = 0
prod = ''
menor = 100000
while True:
    nome = str(input('Nome do Produto: ')).strip()
    valor = float(input('Preço: R$'))
    compra += valor
    if valor > 1000:
        cont += 1
    if valor < menor:
        menor = valor
        prod = nome
    while True:
        resp = str(input('Você quer continuar? [S/N] ')).strip().upper()
        if resp not in 'SN':
            print('Opção Invalida')
        else:
            break
    if resp == 'N':
        break
print(f'{"FIM DO PROGRAMA":-^30}')
print(f'O total da compra foi R${compra:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000')
print(f'O produto mais barato foi {prod} que custa R${menor:.2f}')
