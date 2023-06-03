def notas(*nota, sit = False):
    ficha = dict()
    maior = soma = c1 = 0
    menor = 11
    for c in nota:
        soma += c
        c1 += 1
        if c < menor:
            menor = c
        if c > maior:
            maior = c
    ficha['total'] = c1
    ficha['maior'] = maior
    ficha['menor'] = menor
    ficha['media'] = soma / ficha['total']
    if sit == True:
        if ficha['media'] >= 7.0:
            ficha['situacao'] = 'APROVADO'
        else:
            ficha['situacao'] = 'REPROVADO'
    return ficha


resp = dict()

resp = notas(3.5, 2, 6.5, sit = True)
print(resp)