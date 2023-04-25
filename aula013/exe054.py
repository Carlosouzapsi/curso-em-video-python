from datetime import date
qtd_maiores = 0
qtd_menores = 0
ano_atual = date.today().year
for c in range(0, 3):
    ano_nascimento = int(
        input(f'Digite o ano de nascimento da pessoa {c + 1}: '))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        qtd_maiores += 1
    else:
        qtd_menores += 1
print(f'Maiores de idade: {qtd_maiores}')
print(f'Menores de idade: {qtd_menores}')
