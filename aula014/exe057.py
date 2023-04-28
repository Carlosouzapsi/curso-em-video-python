# n = False
# while n == False:
#     sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
#     if sexo in 'M':
#         n = True
#     if sexo in 'F':
#         n = True
# print(f'O sexo informado foi: {sexo}')

sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(
        input('Dados inválidos. Por favor,  informe seu sexo: [M/F] ')).strip().upper()[0]
print(f'O sexo informado foi: {sexo} e foi registrado com sucesso.')
