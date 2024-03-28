# Importações
import random

# Declarando variaveis
numeroChute = 0
chute = 0
numero = random.randint(0, 9)
print("Vamos jogar um jogo...")
i = 0

# Estrutura de chutes para erros e acertos
while numero != numeroChute:
    numeroChute = int(input("Chute um numero de 1 a 9: "))
    i = i + 1  # incrementa em 1 o valor de i

    if numeroChute < numero:
        print("chutou baixo, tente novamente!")
    elif numeroChute > numero:
        print("Chutou Alto, tente novamente!")
    else:
        print(f"show de bola, você acertou em {i} tentativas !")
