from emoji import emojize
from random import choice
print('=' * 10)
print('JOKEMPO')
print('=' * 10)

resp = int(input('Vamos jogar? \n[1]Sim ou [2]Não: '))
if resp == 2:
    print(emojize("Tudo bem e tenha um bom dia! :thumbs_up:"))
elif resp == 1:
    escolha = int(input(emojize('[1]Pedra :rock:\n[2]Papel :roll_of_paper:\n[3]Tesoura :scissors:\nFaça sua escolha: ')))
    maquina = choice(['pedra','papel','tesoura'])
    if escolha == 1 and maquina == 'pedra':
        print(emojize('Usuario::rock: Maquina: :rock:\n\033[1;34mEMPATE\033[m :neutral_face:'))
    elif escolha == 1 and maquina == 'papel':
        print(emojize('Usuário: :rock: x Maquina: :roll_of_paper:\n\033[1;31mVOCÊ PERDEU\033[m :crying_face:'))
    elif escolha == 1 and maquina == 'tesoura':
        print(emojize('Usuario: :rock: x Maquina: :scissors:\n\033[1;32mVOCÊ VENCEU\033[m :grinning_face:'))
    elif escolha == 2 and maquina == 'pedra':
        print(emojize('Usuário: :roll_of_paper: x Máquina: :rock:\n\033[1;32mVOCÊ VENCEU\033[m :grinning_face:'))
    elif escolha == 2 and maquina == 'papel':
        print(emojize('Usuário: :roll_of_paper: x Máquina: :roll_of_paper:\n\033[1;34mEMPATE\033[m :neutral_face:'))
    elif escolha == 2 and maquina == 'tesoura':
        print(emojize('Usuário: :roll_of_paper: x Máquina: :scissors:\n\033[1;31mVOCÊ PERDEU\033[m :crying_face:'))
    elif escolha == 3 and maquina == 'pedra':
        print(emojize('Usuário: :scissors: x Máquina: :rock:\n\033[1;31VOCÊ PERDEU\033[m :crying_face:'))
    elif escolha == 3 and maquina == 'papel':
        print(emojize('Usuário: :scissors: x Máquina: :roll_of_paper:\n\033[1:32mVOCÊ VENCEU\033[m :grinning_face:'))
    elif escolha == 3 and maquina == 'tesoura':
        print(emojize('Usuário: :scissors: x Máquina: :scissors:\n\033[1;34mEMPATE\033[m :neutral_face:'))
    else:
        print('\033[1;31mEscolha Incorreta!\033[m')
else:
    print('\033[1;31Escolha Incorreta!\033[m')
