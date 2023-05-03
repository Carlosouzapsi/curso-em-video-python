numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
while True:
    numero = int(input('Informe um número entre 0 e 10: '))
    if numero >= 0 and numero <= 10:
        print(f'Valor digitado foi: {numeros[numero]}')
        break
    print('Valor inválido, tente novamente!')
