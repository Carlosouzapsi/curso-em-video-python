print('CADASTRO DE PESSOAS')
maiores_18 = 0
homem_maior_18 = 0
qtd_homens = 0
mulher_menor_20 = 0

while True:
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maiores_18 += 1
    if sexo == 'M':
        qtd_homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menor_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos {maiores_18}')
print(f'Total de homems que foram cadastrados {qtd_homens}')
print(f'Total de mulheres com menos de 20 anos {mulher_menor_20}')
