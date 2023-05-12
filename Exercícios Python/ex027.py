nome = str(input('Nome: ')).strip()
n = nome.split()
primeiro = n[0]
ultimo = n[(len(n) - 1)]
print(f'Primeiro nome: {primeiro}\nÚltimo nome: {ultimo}')
