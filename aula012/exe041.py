from datetime import date
dt_nasc = int(input('Informe o ano de nascimento: '))
atual = date.today().year
idade = atual - dt_nasc
if idade <= 9:
    print(
        f'O nadador possui {idade} anos de idade e pertence a categoria MIRIM.')
elif idade <= 14:
    print(
        f'O nadador possui {idade} anos de idade e pertence a categoria INFANTIL.')
elif idade <= 19:
    print(
        f'O nadador possui {idade} anos de idade e pertence a categoria JUNIOR.')
elif idade <= 25:
    print(
        f'O nadador possui {idade} anos de idade e pertence a categoria SENIOR.')
else:
    print(
        f'O nadador possui {idade} anos de idade e pertence a categoria MASTER.')
