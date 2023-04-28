
menor_vinte = 0
idade_grupo = 0
maior_idade_homem = 0
nome_velho = ''
for p in range(1, 4):
    print(f"------- PESSOA {p} -------")
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip()
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff':
        if idade <= 20:
            menor_vinte += 1
    idade_grupo += idade
media_idade = idade_grupo / 4
print(f'A média de idade das pessoas do grupo é {media_idade}')
print(f'O número de mulheres com idade menor que 20 anos é {menor_vinte}')
print(f'O homem mais velho se chama: {nome_velho}')
