cadastro = dict()
lista = list()
media = 0
while True:
    cadastro['nome'] = str(input('Nome: ')).strip()
    while True:
        cadastro['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()
        if cadastro['sexo'] == 'F' or cadastro['sexo'] == 'M':
            break
        else:
            print('Opção Inválida!')
    cadastro['idade'] = int(input('Idade: '))
    media += cadastro['idade']
    lista.append(cadastro.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if resp == 'S' or resp == 'N':
            break
        else:
            print('Opção Inválida')
    if resp == 'N':
        break
idade = media / len(lista)
print(f'- O grupo tem {len(lista)} pessoas.')
print(f'- A média de idade é de {idade:.2f} anos.')
print('- As mulheres cadstradas foram: ', end = '')
for c in range(0, len(lista)):
    if lista[c]['sexo'] == 'F':
        print(f'{lista[c]["nome"]} ', end = '')
print()
print('- A Lista das pessoas que estão acima da media: ')
for c in range(0, len(lista)):
    if lista[c]['idade'] > idade:
        print(f'nome = {lista[c]["nome"]}; ', end = '')
        print(f'sexo = {lista[c]["sexo"]}; ', end = '')
        print(f'idade = {lista[c]["idade"]}')
    print()
print('<< ENCERRADO >>' )

