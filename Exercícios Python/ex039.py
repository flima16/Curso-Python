from datetime import datetime
ano = int(input('Qual o ano do seu nascimento? '))

if datetime.today().year - ano < 18:
    print(f'Você ainda não precisa se alistar falta \033[1;32m{datetime.today().year - ano}\033[m anos para você se alistar.')
elif datetime.today().year - ano == 18:
    print(f'Você está na idade para você se alistar.')
else:
    print(f'Você já passou da idade para se alistar você está \033[1;31m{(datetime.today().year - ano) - 18}\033[m anos atrasado')