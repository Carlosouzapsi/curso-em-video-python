palavras = ("amigo", "amor", "casa", "gato", "chuva",
            "coracao", "festa", "livro", "banana", "computador")
cont = 0
for p in palavras:
    print(f"\nNa palavra {p} temos ", end=' ')
    # lembrar que strings em python se comporta como listas
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=' ')
