#Declaração de Variaveis
x = int(input("Digite um número inteiro para X: "))
y = int(input("Digite um número inteiro para Y: "))

#Declaração da função calculadora
def calculadora():
    operacao = input("""
        Selecione um dos sinais operadores a baixo:
        [+] para Adição
        [-] para Subtração
        [*] para Multiplicação
        [/] para Divisão
        """)

    # Realização do Cálculo
    if operacao == "+":
        calculo = x + y
    elif operacao == "-":
        calculo = x - y
    elif operacao == "*":
        calculo = x * y
    elif operacao == "/":
        calculo = x / y

    resultado = calculo

    # Impressão do resultado na tela
    print(f"O resultado da operação desejada é {resultado} !")

#Chamar a função Calculadora
calculadora()
