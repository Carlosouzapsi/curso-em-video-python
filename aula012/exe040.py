nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'REPROVADO a média do aluno foi: {media}')
elif media >= 5 and media <= 6.9:
    print(f'RECUPERACAO a média do aluno foi: {media}')
elif media >= 7:
    print(f'APROVADO a média do aluno foi: {media}')
