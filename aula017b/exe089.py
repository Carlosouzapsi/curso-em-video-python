alunos = []
while True:
    nome = str(input('Informe o nome do aluno: '))
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    print(f'Aqui: {alunos}')
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar in "N":
        break
print("-=" * 30)
print(f'{"No":<4}{"NOME":<10}{"MEDIA":>8}')
print("-" * 30)
for pos, a in enumerate(alunos):
    print(f"{pos:<4}{a[0]:<10}{a[2]:>8}")
while True:
    aluno = int(input("Mostrar nota de qual aluno? (999 interrompe): "))
    if aluno == 999:
        break
    for pos, a in enumerate(alunos):
        if pos == aluno:
            print("-=" * 30)
            print(f'{"No":<4}{"NOME":<10}{"MEDIA":>8}')
            print("-" * 30)
            print(f"{pos:<4}{a[0]:<10}{a[2]:>8}")
            break
print('Programa encerrado com sucesso! ')
