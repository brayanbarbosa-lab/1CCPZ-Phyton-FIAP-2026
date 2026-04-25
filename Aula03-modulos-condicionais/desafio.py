idade = int(input("Digite a sua idade: "))

if 15 < idade < 18 or idade > 70:
    print('Voto opcional')
elif idade < 16:
    print('Voto proibido')
else:
    print('Voto obrigatório')