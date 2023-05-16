flag = 0

while flag == 0:
    sexo = str(input('Qual seu sexo\n[ M ]Masculino\[ F ]Feminino: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('\033[1;31mOpção Invalida\033[m')
    else:
        flag += 1
if sexo == 'F':
    print(f'Seu sexo é \033[1;35mFeminino\033[m')
else:
    print('Seu sexo é \033[1;34mMasculino\033[m')