dados = dict()
dados['nome'] = str(input('Nome do Aluno: ')).strip()
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
dados['situacao'] = 'Aprovado' if dados['media'] > 7.0 else 'Reprovado'
print(f'O nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["media"]}')
print(f'Situação é igual a {dados["situacao"]}')

