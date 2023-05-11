# Dicionários em python

# declarando um dicionario:
pessoas = {}
# declarando e preenchendo um dicionario com dados:
pessoas = {'nome': "Carlos", "sexo": "M", "idade": 22}
print(pessoas)
# imprimindo um elemento em especifico:
print(pessoas["nome"])
# formatando e imprimindo mais de um elemento:
print(f"{pessoas['nome']} tem {pessoas['idade']} anos.")
# imprimindo somente as chaves
print(pessoas.keys())
# imprimindo somente os values
print(pessoas.values())
# imprimindo os items (chave e valor) de um dicionario:
print(pessoas.items())
