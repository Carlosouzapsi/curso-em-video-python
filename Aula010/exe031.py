distancia = float(input('Qual é a distância de sua viagem? '))
print(f'Você está prestes a começr uma viagem de {distancia:.2f}km')
'''
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
'''
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'Preço final da viagem R${preco:.2f}')
