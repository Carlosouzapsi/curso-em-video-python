from time import sleep

for e in range(10, -1, -1):  # termo do meio precisa ser -1 senão é ignorado!
    sleep(1)
    print(e)
