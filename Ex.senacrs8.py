# Escreva um algoritmo que leia o código de um determinado produto
# e mostre sua classificação.

# Declaração de variável Código do produto
Codigo_produto = int(input("Insira o código do produto: "))

# Verificação de Código e comparação com o tipo de Produto
if Codigo_produto == 1:
    print("Alimento não perecível")
elif Codigo_produto == 2 or Codigo_produto == 3 or Codigo_produto == 4:
    print("Alimento perecível")
elif Codigo_produto == 5 or Codigo_produto == 6:
    print("Vestuário")
elif Codigo_produto == 7:
    print("Higiene pessoal")
elif Codigo_produto >= 8 and Codigo_produto <= 15:
    print("Limpeza e utensílios domésticos")
else:
    print("Inválido!")
