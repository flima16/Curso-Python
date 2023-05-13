from datetime import datetime
print('=' * 35)
print('  Confederação Nacional de Natação')
print('=' * 35)
ano = int(input('Ano de Nascimento: '))
print('Você pertence a categoria:')
ano = datetime.today().year - ano
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