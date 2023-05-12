print('+=+' * 10)
print('   Analisador de Triângulo    ')
print('+=+' * 10)
r1 = int(input('Primeira Segmento: '))
r2 = int(input('Segunda Reta: '))
r3 = int(input('Terceira Reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos {r1},{r2},{r3} formam um triângulo')
else:
    print(f'Os segmentos {r1},{r2},{r3} não formam um triângulo')
