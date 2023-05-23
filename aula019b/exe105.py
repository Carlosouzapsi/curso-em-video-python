def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre situação da turma
    """
    alunos_info = dict()
    notas = n
    media = sum(notas) / len(notas)
    maior_nota = 0
    menor_nota = 0
    for c in range(0, len(notas)):
        if c == 0:
            maior_nota = c
        else:
            if maior_nota < notas[c]:
                maior_nota = notas[c]
                menor_nota = notas[c]
            if menor_nota > notas[c]:
                menor_nota = notas[c]
        alunos_info['total'] = len(notas)
        alunos_info['maior'] = maior_nota
        alunos_info['menor'] = menor_nota
        alunos_info['media'] = media
        if sit == True:
            if alunos_info['media'] >= 7:
                alunos_info['situacao'] = "BOA"
            if alunos_info['media'] >= 5:
                alunos_info['situacao'] = "RAZOAVEL"
            else:
                alunos_info['situacao'] = "RUIM"
    return alunos_info


# programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
