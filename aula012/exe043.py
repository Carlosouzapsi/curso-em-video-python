print("=" * 25)
peso = float(input('Informe o peso da pessoa: '))
altura = float(input('Informe a altura da pessoa: '))
print("=" * 25)
imc = peso / (altura * altura)
if imc < 18.5:
    print('Esta pessoa está muito abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Esta pessoa está dentro do peso ideal')
elif imc <= 25 and imc <= 30:
    print('Você está com sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade mórbida')
elif imc >= 40:
    print('Você está em obesidade mórbida, cuidado!')
