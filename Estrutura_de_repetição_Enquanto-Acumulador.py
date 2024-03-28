import time
i = 0
while i < 7: #Enquanto i for menor que 10, repete
    i = i + 1 #incrementa em 1 o valor de i
    print(f"o valor de i atualmente é {i}:") #mostra o valor de i
    time.sleep(0.5)


x = 0
while x < 7:
    x = x + 1
    acumulador = x * 5
    print(acumulador)
    time.sleep(0.5)