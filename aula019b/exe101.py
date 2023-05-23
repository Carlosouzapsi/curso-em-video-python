

def voto(ano_nasc):
    # escopo de importação
    from datetime import date
    idade = date.today().year - ano_nasc
    if idade < 16:
        return f"Com {idade}: NÃO VOTA."
    elif 16 <= idade < 18 or idade > 65:  # jeito de escrever no python!
        return f"Com {idade}: VOTO OPCIONAL."
    elif idade >= 18 and idade < 65:
        return f"Com {idade}: VOTO OBRIGATÓRIO."


nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))
