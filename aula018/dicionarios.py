# # Dicionários em python

# # declarando um dicionario:
# pessoas = {}
# # declarando e preenchendo um dicionario com dados:
# pessoas = {'nome': "Carlos", "sexo": "M", "idade": 22}
# print(pessoas)
# # imprimindo um elemento em especifico:
# print(pessoas["nome"])
# # formatando e imprimindo mais de um elemento:
# print(f"{pessoas['nome']} tem {pessoas['idade']} anos.")
# # imprimindo somente as chaves
# print(pessoas.keys())
# # imprimindo somente os values
# print(pessoas.values())
# # imprimindo os items (chave e valor) de um dicionario:
# print(pessoas.items())

# # Usando o for:
# for k in pessoas.keys():
#     print(k)
# for v in pessoas.values():
#     print(v)
# for k, v in pessoas.items():
#     print(f"{k} = {v}")

# Utilizando listas com dicionarios:
brasil = []
estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2 = {"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)

# Printando a lista com elementos que são um dicionário
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    # para copiar dicionarios no python é necessário usar o metodo .copy()
    brasil.append(estado.copy())

# percorrendo o dicionario dentro de uma lista
for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")
    # ou

    # for v in e.items():
    #     print(v, end=" ")
