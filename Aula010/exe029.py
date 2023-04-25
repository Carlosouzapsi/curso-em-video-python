velocidade_atual = float(input('Informe a velocidade de carro:'))
velocidade_permitida = 80
multa = (velocidade_atual - velocidade_permitida) * 7
if velocidade_atual > velocidade_permitida:
    print(f'Você foi multado! A sua velocidade era R${velocidade_atual}')
    print(f'O valor da sua multa é: {multa}')
print(
    f'Sua velocidade era {velocidade_atual}km/h, tenha um bom dia dirija com seg.')
