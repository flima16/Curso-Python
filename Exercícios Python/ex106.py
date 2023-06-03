from time import sleep

cores = {'branco' : '\033[7;40m',
             'verde' : '\033[1;42m',
             'vermelho' : '\033[1;41m',
             'azul' : '\033[1;44m',
             'fim' : '\033[m'
            }

def mensagem(cor,msg):
    print(cor, end = '')
    print('~' * len(msg), end = '')
    print(cores['fim'])
    print(cor, end = '')
    print(msg, end = '')
    print(cores['fim'])
    print(cor, end = '')
    print('~' * len(msg), end = '')
    print(cores['fim'])

def manual(cor, msg):
    print(cor, end = '')
    help(msg)
    print(cores['fim'])


while True:
    mensagem(cores['verde'], ' SISTEMA DE AJUDA PyHELP ')
    funcao = str(input('Função ou Biblioteca > ')).strip().lower()
    if funcao != 'fim':
        sleep(0.5)
        mensagem(cores['azul'],f' Acessando o manual do comando {funcao} ')
        manual(cores['branco'], funcao)
    else:
        mensagem(cores['vermelho'], ' ATÉ LOGO ')
        break
