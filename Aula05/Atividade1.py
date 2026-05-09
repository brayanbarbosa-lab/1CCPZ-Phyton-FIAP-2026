'''Duplas - Repetições encadeadas'''

nomes = ["ana", "leo", "jo", "bia"]

for i in range(len(nomes) - 1):
    for j in range(i+1, len(nomes)):
        print(nomes[i], nomes[j])
