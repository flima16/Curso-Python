flag = True
sexo = resp = 'A'
c1 = c2 = c3 = 0
while True:
    print('-' * 20)
    print(f'{"CADASTRE UMA PESSOA":^20}')
    print('-' * 20)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
       sexo = str(input('Sexo [M/F]: ')).strip().upper()
       if sexo != 'M' and sexo != 'F':
            print('Opção Inválida')
       elif sexo == 'M':
            c1 += 1
       elif idade < 20:
            c2 += 1
    sexo = 'A'
    if idade > 18:
        c3 += 1
    print('-' * 20)
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp != 'S' and resp != 'N':
            print('Opção Inválida')
    if resp == 'N':
        break
    resp = 'A'
print(f'{"FIM DO PROGRAMA":=^40}')
print(f'Total de pessoas com mais de 18 anos: {c3}')
print(f'Ao todo temos {c1} homens cadastrados')
print(f'E temos {c2} mulheres com menos de 20 anos.')