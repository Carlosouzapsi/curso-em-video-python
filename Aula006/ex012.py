preco_produto = float(input('Informe o valor do produto: R$'))
desconto = (preco_produto * 5) / 100
preco_final = preco_produto - desconto
print(f'Preço final do produto: R${preco_final:.2f}')
