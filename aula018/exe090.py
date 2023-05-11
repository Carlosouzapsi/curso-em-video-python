aluno = dict()
aluno['nome'] = str(input("Nome do aluno: "))
aluno['media'] = float(input("Media do aluno: "))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] < 7:
    aluno['situacao'] = 'Reprovado'

print("-=" * 30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
