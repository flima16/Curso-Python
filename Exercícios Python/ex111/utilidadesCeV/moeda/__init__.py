def metade(p, sit = False):
    if sit == True:
        return moeda(p / 2)
    else:
        return p / 2

def dobro(p, sit = False):
    if sit == True:
        return moeda(p * 2)
    else:
        return p * 2

def aumentar(p, n, sit = False):
    if sit == True:
        return moeda(p + (p * (n / 100)))
    else:
        return p + (p * (n / 100))

def diminuir(p, n, sit = False):
    if sit == True:
        return moeda(p - (p * (n / 100)))
    else:
        return p - (p * (n / 100))

def moeda(p):
    return f'R${p:.2f}'.replace('.', ',')

def resumo(p, n, m):
    linha()
    print(f'{"Resumo do Valor":^20}')
    linha()
    print('Preço Analisado: ', end = '')
    print(f'{moeda(p):>10}')
    print('Dobro do Preço: ', end = '')
    print(f'{dobro(p, True):>12}')
    print('Metade do preço: ', end = '')
    print(f'{metade(p, True):>10}')
    print(f'{n}% de aumento: ', end = '')
    print(f'{aumentar(p, n, True):>11}')
    print(f'{m}% de redução: ', end = '')
    print(f'{diminuir(p,n, True):>11}')
    linha()

def linha():
    print('-' * 25)