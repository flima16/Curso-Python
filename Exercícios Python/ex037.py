print('=+' * 10)
print('\033[4;34mConversão Numérica\033[m')
print('=+' * 10)
conv = int(input('[1]Binário\n[2]Octal\n[3]Hexadecimal\nQual é a sua escolha: '))
num = int(input('Digite um número: '))

if conv == 1:
    print(f"O número \033[1;33m{num}\033[m em decimal é igual a \033[1;31m{bin(num)}\033[m em binario")
elif conv == 2:
    print(f'O número \033[1;33m{num}\033[m em decimal é igual a \033[1;34m{oct(num)}')
else:
    print(f'O número \033[1;33m{num}\033[m em decimal é igual a \033[1;33m{hex(num)}\033[m')