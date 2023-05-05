lista = []
while True:
    numero = int(input('Informe um número: '))
    if numero not in lista:
        lista.append(numero)
    else:
        print('Número já foi adicionado a lista, tente outro valor!')
    r = str(input("Quer continuar? ")).strip().upper()[0]
    if r in 'N':
        break
lista.sort()
print(f' valores da lista de forma ordenada: {lista}')
