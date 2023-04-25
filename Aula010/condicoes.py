"""
CONDIÇÕES PARTE - 01
"""

# Mensagem Simples:

# nome = str(input('Qual é o seu nome? '))
# if nome == 'Gustavo':
#     print(f'Que nome lindo Gustavo!')
# print(f'Bom dia {nome}!')

# Calcule a média das notas:
# n1 = float(input('Informe a nota 1: '))
# n2 = float(input('Informe a nota 2: '))
# media = (n1 + n2) / 2
# print(f'A média dos alunos é: {media}')

# If nota for maior que 6
n1 = float(input('Informe a nota 1: '))
n2 = float(input('Informe a nota 2: '))

media = (n1 + n2) / 2
if media >= 6:
    print('Sua média foi boa parabéns!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
