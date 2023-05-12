nome = str(input('Digite o nome da cidade:')).strip()
n = nome.split()
print(f'A cidade de {nome} começa com nome Santo?')
print(n[0].upper() == 'SANTO')