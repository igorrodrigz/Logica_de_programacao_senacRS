print(20*'~~')
print('          BEM VINDO A LOJA MR.SHOP!       ')
valor = float(input('Qual o valor total da compra?'))

forma = float(input('''Insira a forma de pagamento?

[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço normal
[4] 3x ou mais no cartão: 10% de juros'''))

if forma == 1:
    desconto = valor * 10/100
    valorTotal = valor - desconto
    print(f"O Cliente deverá pagar R${valorTotal}0")
elif forma == 2:
    desconto = valor * 5/100
    valorTotal = valor - desconto
    print(f"O Cliente deverá pagar R${valorTotal}0")
elif forma == 3:
    print(f"O Cliente deverá pagar R${valor}0")
elif forma == 4:
    juros = valor * 10/100
    valorTotal = valor + juros
    print(f"O Cliente deverá pagar R${valorTotal}0")

print(20*"~~")
print("Obrigado por comprar na MR.SHOP volte sempre")
print(20*"~~")