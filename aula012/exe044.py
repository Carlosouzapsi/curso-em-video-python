print(f'{"Lojas Carlos":=^40}')
preco = float(input('Preço das compras R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque    
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
opcao = int(input('Informe a opção de pagamento: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(
        f'Sua compra será parcelada em 2x de {parcela} de total R${total} SEM JUROS')
elif opcao == 4:
    total = preco + ((preco * 20) / 100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print(
        f'Sua compra será parcelada em {totparc}x de total de R${total} COM JUROS')
print(f'Sua compra de valor R${preco} vai acabar custando R${total}')
