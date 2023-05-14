print('=' * 10)
print('Triângulo')
print('=' * 10)
cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m'}


r1 = int(input('Primeira Reta: '))
r2 = int(input('Segunda Reta: '))
r3 = int(input('Terceira Reta: '))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r2 + r1):
    if r1 == r2 == r3:
        print(f"As retas [{cores['azul']}{r1}{cores['limpa']}] [{cores['amarelo']}{r2}{cores['limpa']}] [{cores['vermelho']}{r3}{cores['limpa']}] formam um triângulo equilátero.")
    elif (r1 == r2 and r2 != r3) or (r2 == r3 and r1 != r3) or (r1 == r3 and r1 != r2):
        print(f"As retas [{cores['azul']}{r1}{cores['limpa']} [{cores['amarelo']}{r2}{cores['limpa']}] [{cores['vermelho']}{r3}{cores['limpa']}] forma um triângulo isósceles.")
    else:
        print(f"As retas [{cores['azul']}{r1}{cores['limpa']}] [{cores['amarelo']}{r2}{cores['limpa']}] [{cores['vermelho']}{r3}{cores['limpa']}] forma um triângulo escaleno.")
else:
    print(f"As retas [{cores['azul']}{r1}{cores['limpa']}] [{cores['amarelo']}{r2}{cores['limpa']}] [{cores['vermelho']}{r3}{cores['limpa']}] não formam um triângulo.")