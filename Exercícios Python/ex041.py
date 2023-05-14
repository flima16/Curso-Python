from datetime import datetime
print('=' * 35)
print('  Confederação Nacional de Natação')
print('=' * 35)
ano = int(input('Ano de Nascimento: '))
ano = datetime.today().year - ano
print(f'O aluno possui \033[1;34m{ano}\033[m anos de idade.')
print('Você pertence a categoria:' , end = '')
if ano <= 9:
    print('\033[1;34mMIRIM\033[m')
elif ano > 9 and ano <= 14:
    print('\033[1;34mINFANTIL\033[m')
elif ano > 14 and ano <= 19:
    print('\033[1;34mJÚNIOR\033[m')
elif ano > 19 and ano <= 20:
     print('\033[1;34mSÊNIOR\033[m')
else:
    print('\033[1;34MASTER\033[m')