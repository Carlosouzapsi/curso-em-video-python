valores = []
for valor in range(0, 4):
    valores.append(int(input('Informe um número: ')))
print(f"Valores sendo armazenados na lista: {valores}")
print(
    f"Maior valor dentro da lista: {max(valores)} na posição {valores.index(max(valores))}")
print(
    f"Menor valor dentro da lista: {min(valores)} na posição {valores.index(min(valores))}")
