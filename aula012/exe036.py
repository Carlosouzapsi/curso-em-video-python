casa = float(input('Qual o valor total da casa? R$'))
salario = float(input('Qual o salario do comprador? '))
anos = int(input('Em quantos anos a casa será paga? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(
    f'Para pagar uma casa de R${casa:.2f} a prestação será {anos} anos', end='')
print(f'A prestação será de um R${prestacao:.2f}')
if prestacao < - minimo:
    print('Empréstimo pode ser Concedido!')
else:
    print('Empréstimo Negado!')
