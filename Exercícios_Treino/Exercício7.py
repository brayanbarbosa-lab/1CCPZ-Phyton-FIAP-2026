''' Leia 2 valores A e B, que correspondem a 2 notas de um aluno. A seguir calcule e informe a média
ponderada do aluno, sabendo que a nota A tem peso 4 e a nota B tem peso 6.
▪ Exemplo: nota a * 4 e nota b * 6'''

notaa = float(input("Digite a primeira nota do aluno:"))

notab = float(input("Digite a segunda nota do aluno:"))

print(f"A média pondera do aluno é: {((notaa*4)+(notab*6))/(6+4)}")