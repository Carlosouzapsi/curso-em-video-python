nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
qtd_letras = len(nome.replace(" ", ""))
print(f'Seu nome tem {qtd_letras} letras')
