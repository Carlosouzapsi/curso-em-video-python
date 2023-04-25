# # ex005a
# import math

# n1 = int(input('Digite um numero: '))
# antecessor = n1 - 1
# sucessor = n1 + 1
# print(f'Antecessor: {antecessor}')
# print(f'Sucessor: {sucessor}')

# # ex005b
# n1 = int(input('Digite um numero: '))
# dobro = n1 * 2
# raizQ = math.sqrt(n1) => pow(2, 1/2) -> potencia
# print(f'Dobro: {dobro}')
# print(f'Sucessor: {raizQ:.3}')  # reduzindo o numero de valores decimais.

# ex007c
# n1 = int(input('Digite a segunda nota: '))
# n2 = int(input('Digite a segunda nota: '))
# media = (n1 / n2) / 2
# print(f'A média final do estudante foi: {media:.2}')

# ex008c
# medida = float(input('Um distância em metros: '))
# conversor_cm = medida * 100
# conversor_mm = medida * 1000
# formatei com duas casas decimais
# print(f'Valor convertido para cm: {conversor_cm:.2f}')
# print(f'Valor convertido para mm: {conversor_mm:.2f}')

# ex009c
# print('-' * 12)
# numero_tabuada = int(input('Informe o número que você deseja ver a tabuada: '))
# for i in range(numero_tabuada, 11):
#     print(f'{numero_tabuada} x {i} = {i * numero_tabuada}')
# print('-' * 12)

# ex010c
# dinheiro_carteira = float(input('Informe o dinheiro na carteira: R$'))
# cotacao_dolar = 5.12
# dolar_comprado = dinheiro_carteira / cotacao_dolar
# print(f'Consegui comprar: US$ {dolar_comprado:.2f}')

# ex011c
altura = float(input('Informe a altura: '))
largura = float(input('Informe a largura: '))
area = largura * altura
print(
    f'Sua parede tem a dimensão de {altura} x {largura} e sua área é {area}m2')
tinta = area / 2
print(f'Para pintar essa parede você vai precisar de litros {tinta}')
