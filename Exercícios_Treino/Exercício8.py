'''Neste problema, deve-se ler o nome de uma peça que chamaremos de peça1, o número de peças1 que
o usuário quer, o valor unitário de cada peça1, o nome de uma peça2, o número de peças2 e o valor
unitário de cada peça2. Após, calcule e mostre o valor a ser pago.
'''



peça1 = input("Digite o nome da primeira peça:")
quantidade1 = float(input(f"Qual a quantidade de {peça1}s que deseja?"))
valor1 = float(input(f"Qual o valor unitário da {peça1}?"))
total1 = quantidade1*valor1

peça2 = input("Digite o nome da segunda peça:")
quantidade2 = float(input(f"Qual a quantidade de {peça2}s que deseja?"))
valor2 = float(input(f"Qual o valor unitário da {peça2}?"))
total2 = quantidade2*valor2

valorfinal = total1 + total2

print(f"O valor de {peça1}: {total1}\n "
      f"O valor de {peça2}: {total2}\n "
      f"O total a ser pago é: {valorfinal}")

'''
feito com for

total = 0

for i in range(2):
    nome = input(f"Digite o nome da peça {i+1}: ")
    quantidade = float(input(f"Qual a quantidade de {nome}s que deseja? "))
    valor = float(input(f"Qual o valor unitário da {nome}? "))

    subtotal = quantidade * valor
    total += subtotal

    print(f"Valor de {nome}: {subtotal}\n")

print(f"Total a ser pago: {total}")
'''