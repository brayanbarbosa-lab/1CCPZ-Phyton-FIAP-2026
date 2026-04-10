idade = 20

maior_idadde = idade >= 18
print(maior_idadde, type(maior_idadde))
print() #pula uma linha

verifica_email = True
verifica_senha = True

login = verifica_email and verifica_senha

if not login:
    print("Errou, lixo")

print()

nota_final = 2.0

if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")

print("FIM")
