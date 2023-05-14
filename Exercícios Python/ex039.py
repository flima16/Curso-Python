from datetime import datetime
print('=+' * 15)
print('    ALISTAMENTO MILITAR')
print('=+' * 15)
sexo = str(input('Qual seu gênero\n[ M ]Masculino\n[ F ]Feminino\nGenero: ')).upper()
if sexo == 'M':
    ano = int(input('Qual o ano do seu nascimento? '))
    if datetime.today().year - ano < 18:
        print(f'Você ainda não precisa se alistar falta \033[1;32m{18 - (datetime.today().year - ano)}\033[m anos para seu alistamento.')
        print(f'Seu alistamento será em \033[1;34m{ano + 18}\033[m')
    elif datetime.today().year - ano == 18:
        print(f'Você está na idade para se alistar.')
    else:
        print(f'Você já passou da idade para se alistar. Você está \033[1;31m{(datetime.today().year - ano) - 18}\033[m anos atrasado')
        print(f'Seu alistamento foi em \033[1;34m{ano + 18}\033[m')
else:
    print('Você não é obrigada se alistar.')