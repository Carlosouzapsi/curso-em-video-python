from datetime import datetime

pessoa = {}
pessoa['nome'] = str(input('Informe o nome da pessoa: '))
pessoa['nasc'] = int(input('Informe o ano de nascimento da pessoa: '))
pessoa['ctps'] = int(input('Informe o numero do CTPS: (0 não tem)'))
if pessoa['ctps'] != 0:
    pessoa['cont'] = int(input('Informe o ano da contratação: '))
    pessoa['salario'] = float(input('Informe o salário da pessoa: R$'))
    pessoa['idade'] = datetime.now().year - pessoa['nasc']
    pessoa['aposentadoria'] = pessoa['idade'] + \
        ((pessoa['cont'] + 35) - datetime.now().year)
print(f'-=' * 30)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
