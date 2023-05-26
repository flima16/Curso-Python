from operator import neg
def analise(a, b, c):
    if (a < b and c > 0) or (a > b and c < 0):
        return c
    elif a < b and c < 0:
        return neg(c)
    elif a > b and c > 0:
        return neg(c)
    elif a > b and c == 0:
        return -1
    else:
        return 1

def listra(a, b, c):
    print('-=' * 30)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    print('-=' * 30)


def analise1(e,f):
    if e < f:
        f += 1
        return f
    else:
        f -= 1
        return f

def contagem(a, b, c):
    listra(a, b, c)
    for d in range(a, analise1(a, b), analise(a, b, c)):
        print(d, end = ' ')
    print()

contagem(1, 10, 1)
contagem(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contagem(a, b, c)