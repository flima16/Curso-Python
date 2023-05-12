
numero = int (input('Digite um valor entre 0 a 9999: '))
milhar = (numero // 1000)
cent = ((numero // 100) % 10)
dez = ((numero // 10) % 10)
unidade = (numero % 10)
print(f'unidade:{unidade}\ndezena:{dez}\ncentena:{cent}\nmilhar:{milhar}\n\n')

