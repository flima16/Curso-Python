dia = int(input('Quantos dias alugados? '))
Km = int(input('Quantos Km rodados? '))
print(f'O total a pagar é de R${(dia * 60) + (0.15 * Km):.2f}')