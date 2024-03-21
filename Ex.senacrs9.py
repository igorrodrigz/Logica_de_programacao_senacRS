idade_nadador = int(input("Insira a idade do Nadador: "))

if idade_nadador >= 5 and idade_nadador <=7:
    print("Infantil A")
if idade_nadador >= 8 and idade_nadador <=10:
    print("Infantil B")
if idade_nadador >= 11 and idade_nadador <=13:
    print("Juvenil A")
if idade_nadador >= 14 and idade_nadador <= 17:
    print("Juvenil B")
if idade_nadador >= 18 and idade_nadador <= 59:
    print("Adulto")
if idade_nadador >= 60:
    print("Master")