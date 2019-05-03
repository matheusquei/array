estados = [input("\nDigite o primeiro estado: ").upper(),
           input("\nDigite o segundo estado: ").upper(),
           input("\nDigite o terceiro estado: ").upper()]

populacao = [int (input("\nDigite a população do primeiro estado: ")),
             int (input("\nDigite a população do segundo estado: ")),
             int (input("\nDigite a população do terceiro estado: "))]


print(estados)

print("\nSoma total de toda a população é: ", populacao[0] + populacao[1] + populacao[2])

print("\nA média da população é: ", populacao[0] + populacao[1] + populacao[2] / 3)