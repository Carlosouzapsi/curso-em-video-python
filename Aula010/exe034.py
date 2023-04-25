salario = float(input('Informe o salário do funcionário: '))
if salario <= 1250:
    novo = salario + ((salario * 15) / 100)
else:
    novo = salario + ((salario * 10) / 100)
print(f'O novo salário do funcionário é R${novo:.2f}')
