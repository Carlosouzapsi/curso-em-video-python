# Strip elimina os espaços antes e depois
cidade = str(input('Digite o nome da cidade: ')).strip()
comeca_com_santo = cidade[:5].upper() == 'SANTO'
print(f'Cidade começa com a palavra Santo? {comeca_com_santo}')
