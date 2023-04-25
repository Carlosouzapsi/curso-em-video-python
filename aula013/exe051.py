primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão da PA: '))
decimo = primeiro_termo + (10 - 1) * razao
for termos in range(primeiro_termo, decimo, razao):
    print(termos, end=' ')
print('ACABOU')
