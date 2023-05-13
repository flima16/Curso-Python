nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('\033[1;31mREPROVADO!\033[m')
elif media >= 5.0 and media < 7.0:
    print('\033[1;34mRECUPERAÇÃO\033[m')
else:
    print('\033[1;32mAPROVADO!\033[m')