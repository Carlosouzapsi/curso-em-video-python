# FORMAS DE CRIAR UMA LISTA VAZIA:
# valores = []
# valores = list()
num = [1, 2, 3, 4, 5]
print(f'Lista normal: {num}')
num[0] = 'Olá Mundo!'  # valor é mutável
print(f'Lista alterada: {num}')
# Adicionar elemento no final (append(x)) :
num.append(7)
print(f'Novo valor no final: {num}')
num = [1, 2, 3, 4, 5]
# Ordenando em forma crescente ou alfabetica
num.sort()
print(f'Ordenada: {num}')
num.sort(reverse=True)
print(f'Ordenando ao contrárip: {num}')
# Retornando numero de elementos com a func len()
print(f'A lista possui {len(num)} no total de elementos')
# inserindo valores com insert
num = [1, 2, 3, 4, 5]
num.insert(2, 0)
print(f'Na posição 2 inseri o novo valor zero com insert: {num}')
# removendo elemento com pop:
num = [1, 2, 3, 4, 5]
num.pop()
print(
    f'Sem utilizar parametros no pop() eu removo o ultimo elemento de num {num}')
# removendo com remove (procura primeira ocorrencia e remove)
num = [1, 2, 3, 4, 2, 5]
num.remove(2)
print(f' Removi o primeiro 2 que apareceu! Olha: {num}')
# usando um exemplo de condicional com remove
print('Será que achei o número? ')
num = [1, 2, 3]
if 4 in num:
    num.remove(4)
else:
    print(f'Não achei o numero 4!')

# Mais exemplos:
valores = []
valores.append(1)
valores.append(2)
valores.append(3)

print('Imprimindo uma lista usando o for: ')
for v in valores:
    print(f'{v}', end=" ")
print('pegando a posicao com enumerate')
for c, v in enumerate(valores):
    print(f'Na posição{c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

print('Inputando valores e dando append na lista: ')
for cont in range(0, 2):
    valores.append(int("Digite um valor: "))
for c, v in enumerate(valores):
    print(f'Na posição{c} encontrei o valor {v}!')
print('Cheguei ao final da lista que eu digitei!')

# Peculiaridade do python:
a = [2, 3, 4, 7]
b = a
b[2] = 8
print("O python vai mexer nas duas listas!!! =O")
print(f'Lista A: {a}')
print(f'Lista B: {b}')
