print('=+' * 10)
print('\033[4;34mConversão Numérica\033[m')
print('=+' * 10)
num = int(input('Digite um número: '))
print('Escolha a base de conversão\n')
conv = int(input('[ 1 ]Binário\n[ 2 ]Octal\n[ 3 ]Hexadecimal\nSua opção: '))
if conv == 1:
    print(f"O número \033[1;33m{num}\033[m em decimal é igual a \033[1;31m{bin(num)[2:]}\033[m em binario")
elif conv == 2:
    print(f'O número \033[1;33m{num}\033[m em decimal é igual a \033[1;34m{oct(num)[2:]}')
elif conv == 3:
    print(f'O número \033[1;33m{num}\033[m em decimal é igual a \033[1;33m{hex(num)[2:]}\033[m')
else:
    print('\033[31mOpção Inválida\033[m')