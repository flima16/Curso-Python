print('=' * 20)
print('    \033[35;40mEmpréstimo\033[m   ')
print('=' * 20)

casa = float(input('Qual o valor da casa: '))
sal = float(input('Qual é o seu salário: '))
ano = int(input('Quantos anos irá pagar: '))

parcela = sal * 0.3
emprestimo = casa / (ano * 12)
if parcela < emprestimo:
    print('\033[1;031mEMPRÉSTIMO NEGADO!\033[m')
    print(f'Parcela \033[1;4mO empréstimo de {emprestimo:.2f}\033[m ao mês excede os 30% do valor do salário \033[1;4m{parcela:.2f}\033[m')
else:
    print('\033[34mEMPRÉSTIMO APROVADO\033[m')
    print(f'O empréstimo de \033[1;4m{emprestimo:.2f}\033[m ao mês não ultrapassa os 30% do valor do salário \033[1;4m{parcela:.2f}\033[m')