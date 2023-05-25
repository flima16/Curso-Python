from datetime import datetime
cadastro = dict()

cadastro['nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de Nascimento: '))
cadastro['idade'] = datetime.today().year - nasc
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
while cadastro['ctps'] != 0:
    cadastro['ano'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Sálario: '))
    cadastro['aposentadoria'] = cadastro['ano'] - nasc + 35
    break
print('-=' * 40)
for k,v in cadastro.items():
    print(f'{k} tem o valor {v}')