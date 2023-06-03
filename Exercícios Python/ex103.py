def ficha(nome = ' ', gols = ' '):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '' or gols.isalpha():
        gols = 0
    print(f'O jodador {nome} fez {gols} gols no campeonato')



print('-' * 15)
nome = str(input('Nome do Jogador: ')).strip()
gol = str(input('Número de Gols: ')).strip()
ficha(nome, gol)