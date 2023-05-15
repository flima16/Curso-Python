print('=' * 20)
print(f'{"PESQUISA":-^20}')
print('=' * 20)
maior = 0
nome = ''
mulheres = 0
media = 0
for c in range(1,5):
    nome = str(input('Qual o seu nome: ')).strip()
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual o seu gênero?\n[ F ]Feminino\n[ M ]Masculino\nOpção: ')).strip().upper()
    print('\n\n')
    if sexo == 'M' and idade > maior:
        nome1 = nome
        maior = idade
    if sexo == 'F' and idade < 20:
        mulheres += 1
    media += idade
print(f'A média de idade do grupo é {media / 4}')
print(f'O homem maios velho do grupo: \033[1;32m{nome1}\033[m')
print(f'Mulheres menores de 20 anos: \033[4;34m{mulheres}\033[m ')