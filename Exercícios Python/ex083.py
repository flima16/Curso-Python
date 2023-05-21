expr = str(input('Digite a expressão: '))

n1 = expr.count('(')
n2 = expr.count(')')

if n1 == n2:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')