frase = str(input('Informe uma frase: ')).upper()
letra_a_vezes = frase.count('A')
print(f'A letra A aparece {letra_a_vezes} vezes na frase')
index_letra_a = frase.find('A')  # primeira posição mais 1
print(f'A primeira vez que a letra A aparece é na posição {index_letra_a}')
last_index_a = frase.rfind('A')  # procura a partir do lado direito
print(f'A ultima vez que a letra aparece é na posição {last_index_a}')
