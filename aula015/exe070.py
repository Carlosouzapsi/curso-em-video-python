print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)
total_compra = 0
contador = 0
produto_mais_1000 = 0
barato = ''
menor_preco = 0
while True:
    nome_prod = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))
    contador += 1
    total_compra += preco
    if preco > 1000:
        produto_mais_1000 += 1
    if contador == 1 or preco < menor_preco:
        menor_preco = contador
        barato = nome_prod
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print(f'Fim do programa!')
print(f"O total gasto na compra foi: RS${total_compra:.2f}")
print(f"Total de produtos acima de R$1000,00 :  {produto_mais_1000}")
print(f"Nome do produto mais barato: {barato}")
