estados=[]

for contador in range (0,3):
    estado=[input("\nDigite a UF: "), int (input("\nDigite a população: "))]
    estados.append(estado)
total_populacao=0
for estado in estados:
    print(estado[0].upper())
    total_populacao+=estado[1]
print("Total de população: " + str(total_populacao))
print("Média de população: " + str(total_populacao/len(estados)))