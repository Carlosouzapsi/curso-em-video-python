from datetime import date
atual = date.today().year
nasc = int(input('Ano do nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print(f'Você precisa se alistar imediatamente!')
if idade < 18:
    saldo = 18 - idade
    print(
        f'O JOVEM AINDA VAI SER ALISTAR NO SERVIÇO MILITAR! FALTAM {saldo} anos')
elif idade <= 18:
    saldo = 18 - idade
    print(
        f'O JOVEM AINDA VAI SER ALISTAR NO SERVIÇO MILITAR! FALTAM {saldo} anos ')
elif idade > 18:
    saldo = 18 - idade
    print(f'O JOVEM JÁ PASSOU DA HORA DO ALISTAMENTO! há {-saldo} anos atrás ')
