def fatorial(n = 1, show = False):
    """
    -> calcula o fatorial de um número.
    :para n: O número a ser calculado
    :para show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n.
    """
    c1 = 1
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return 'Error'
    else:
         for c in range(n, 0, -1):
            c1 *= c
            if show == True:
                print(c, end = ' ')
                if c > 1:
                     print('x', end = ' ')
                else:
                     print('=', end = ' ')
         return c1

print(fatorial(5, show = True))
help(fatorial)