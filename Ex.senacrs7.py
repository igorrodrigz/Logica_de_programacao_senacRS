ano_Nasc = int(input("Insira o ano de nascimento do usuário: "))
ano = 2024
idade = ano - ano_Nasc
print(idade)
if idade >= 16 and idade <= 17:
    print("O usuário possui idade para Votar, mas não pode realizar sua Carteira de Habilitação!")
if idade >= 18:
    print("O usuário possui idade para Votar e Realizar sua Carteira de Habilitação! ")