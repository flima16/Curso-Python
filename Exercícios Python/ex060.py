print('=' * 10)
print(f'{"Fatorial":^10}')
print('=' * 10)
num = 1
fat = int(input('Escolha o valor: '))
print(f'Calculando {fat}! = ', end = '')
if fat == 0 or fat == 1:
    print(1)
else:
    while fat > 0:
       print(fat, end='')
       num *= fat
       if fat != 1:
         print(f' x ', end = '')
       fat -= 1
    print(f'= {num}')

