print('=' * 30)
print('BANCO CEV')
print('=' * 30)
saque = int(input('Informe o valor a ser sacado: '))
total = saque
cedula = 50
total_cedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        print(f'Total de {total_cedulas} cédulas de R${cedula} usadas. ')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0
        if total == 0:
            break
