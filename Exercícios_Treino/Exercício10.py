'''Cabou'''

valor = float(input("Digite um valor:"))

par = valor % 2

if par == 0:
    print (f"Numéro par: {valor}")
else:
    print(f"Número ímpar: {valor}")