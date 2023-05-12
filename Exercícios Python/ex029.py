velo = int(input('Qual a sua velocidade atual? '))
if velo > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print(f'Você deve pagar a multa no valor de R${(velo - 80) * 7.00:.2f}')
print('Tenha um bom dia! Dirija com segurança!')