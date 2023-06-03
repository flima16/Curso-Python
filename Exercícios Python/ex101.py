from datetime import datetime

def votacao(ano):
    idade = datetime.today().year - ano
    print(f'Com {idade} anos: ', end = '')
    if idade < 16:
        return 'Não Vota'
    elif (idade >= 16 and idade < 18) or idade > 65:
        return 'Voto Opcional'
    else:
        return 'Voto Obrigátorio'

print('-' * 20)
nasc = int(input('Em que ano você nasceu? '))
print(f'{votacao(nasc)}')