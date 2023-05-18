tupla = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercardo', 'programador', 'futuro')
frase = ''
for c in range(0, 12):
    frase = tupla[c].upper()
    print(f'Na palavra {frase} temos ', end = '')
    for n in frase:
        if n == 'A' or n == 'E' or n == 'I' or n == 'O' or n == 'U':
            print(f'{n} ', end = '')
    print('\t')

