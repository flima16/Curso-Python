nome = str (input('Nome: ')).strip()
print(f'\nSeu nome em maiusculas é {nome.upper()}')
print(f'Seu nome em minusculas é {nome.lower()}')
nome1 = nome.split()
nome2 = len(nome1[0])
tamanho = len(nome) - (len(nome1) -1)
print(f'Seu nome possui {tamanho} letras')
print(f'O primeiro nome {nome1[0]} possui {nome2} letras')
