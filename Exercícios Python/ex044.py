print('=' * 10)
print('  \033[1;35mCompra\033[m ')
print('=' * 10)

preco = float(input('Preco do Produto: '))
cond = int(input('Condições:\n[1] À vista dinheiro/cheque\n[2] À vista no cartão\n[3]2X no cartão\n[4]3X ou mais no cartão\n'))

if cond == 1:
    print(f'O valor a ser pago é \033[4;34m{preco - (preco * 0.1):.2f}\033[m')
elif cond == 2:
    print(f'O valor a ser pago é \033[4;34m{preco - (preco * 0.05):.2f}\033[m')
elif cond == 3:
    print(f'O valor a ser pago é \033[4;34m{preco:.2f}\033[m')
elif cond == 4:
    print(f'O valor a ser pago é \033[4;34m{preco + (preco * 0.2):.2f}\033[m')
else:
    print('\033[31mOpção Inválida\033[m')
print('\033[32mObrigado e Volte Sempre!\033[m')
