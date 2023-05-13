num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print(f'\033[1;31m{num1}\033[m é maior que \033[1;34m{num2}\033[m')
elif num2 > num1:
    print(f'\033[1;34m{num2}\033[m é maior que \033[1;31m{num1}\033[m')
else:
    print(f'\033[1;31m{num1}\033[m é igual a \033[1;34m{num2}\033[m')