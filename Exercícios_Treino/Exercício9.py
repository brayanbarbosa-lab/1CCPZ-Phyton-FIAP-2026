'''▪ Crie um programa que receba o valor do produto e valor pago.
▪ Calcule o troco a ser pago.
▪ O valor do troco deve ser exibido no terminal.'''

valor = float(input("Qual o valor do produto?:"))
pago = float(input("Quanto foi o dinheiro dado pelo cliente?:"))
troco = pago - valor

if troco > 0:
    print(f"Deve ser dado em dinheiro, {troco} ao cliente")
if troco < 0:
    print(f"O cliente deve pagar em dinheiro mais {troco*-1}")
else:
    print("troco não é necessário")