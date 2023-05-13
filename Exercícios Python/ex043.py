print('=' * 15)
print('Calculo do IMC')
print('=' * 15)

alt = float(input('Sua altura: '))
peso = int(input('Seu peso: '))

imc = peso / alt ** 2

if imc < 18.5:
    (f'Seu IMC é \033[1;32m{imc:.2f}\033[m e você está \033[1;4;34mAbaixo do Peso\033[m')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu IMC está \033[1;32m{imc:.2f}\033[m e você está no \033[1;4;34mPeso Ideal\033[m.')
elif imc > 25 and imc <=30:
    print(f'Seu IMC é \033[1;32m{imc:.2f}\033[m e você está de \033[1;4;34mSobrepeso\033[m.')
elif imc > 30 and imc <= 40:
    print(f'O seu IMC é \033[1;32m{imc:.2f}\033[m e você está com \033[1;4;34mObesidade\033[m')
else:
    print(f'Seu IMC é \033[1;32m{imc:.2f}\033[m e você está com \033[1;4;34Obesidade Mórbida\033[m.')
