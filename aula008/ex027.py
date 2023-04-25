nome_completo = str(input('Informe o nome completo: ')).strip()
nome = nome_completo.split()
print(f'Seu primeiro nome é {nome[0]}')
# print(f'Seu primeiro nome é {nome[-1]}')
print(f'Seu primeiro nome é {nome[len(nome) - 1]}')  # outra forma!
