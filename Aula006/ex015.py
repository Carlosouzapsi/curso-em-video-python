qtd_km = float(input('quantidade de kilometros percorridos: '))
qtd_dias = int(input('Qual o numero de dias que  o carro ficou alugado: '))
preco_dia = 60 * qtd_dias
preco_km = qtd_km * 0.15
preco_total = preco_dia + preco_km
print('=' * 28)
print(f'Preço total dias: R${preco_dia}')
print(f'Preço total km:   R${preco_km:.2f}')
print(f'Preço total:      R${preco_total:.2f}')
print('=' * 28)
