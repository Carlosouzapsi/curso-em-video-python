# EXEMPLO DE TUPLA:
lanche = ("Hamburguer", "Suco", "Pizza", "Pudim")

# FATIAMENTE
print(lanche[2:])  # imprime elemento de index 2 em diante...
print(lanche[:2])  # imprime elemento de index 0 até o 1...
print(lanche[-1])  # imprime o ultimo elemento
print(lanche[-2])  # imprime o penultimo
print(lanche[-2:])  # imprime a partir do index -2 em diante..

# TUPLAS SÃO IMUTAVEIS:
# TypeError: 'tuple' object does not support item assignment
# lanche[1] = 'Refrigerante'

# IMPRIMINDO e percorrendo uma tupla:

# usando FOR IN
# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi pra caramba!')

# usando FOR RANGE
# for cont in range(0, len(lanche)):
#     print(f'lanche {lanche[cont]}')
# print('Comi pra caramba!')

# usando for ENUM:
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')

# usando SORTED sorteio em ordem alfabética
print(sorted(lanche))  # n muda a tupla original

# somando em tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)  # concatena as tuplas a e b em uma nova tupla

# contando recorrencia de elemento em uma tupla:
print(c.count(5))  # qtd vezes que aparece
print(c.index(8))  # qual a pos(index) do elemento de 8
print(c.index(5, 1))  # desloca e conta a partir de determinado elemento.
del (c)  # deleta uma tupla, a tupla é imutavel mas pode ser apagada
