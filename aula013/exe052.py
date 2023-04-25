numero = int(input('Informe um número: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {numero}  fo divisível {tot}  vezes')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')
