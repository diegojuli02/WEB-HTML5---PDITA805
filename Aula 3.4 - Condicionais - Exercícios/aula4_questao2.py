print("Avaliação de filmes informe o titulo do filme e avalie o mesmo em escala de 1 a 5")
filme = input("insira titulo do filme: ")

nota = int(input("informe a nota do filme em escala de 1 a 5: "))

if nota == 5:
    print(f"O título ({filme}) é um filme Excelente!")
elif nota == 4:
    print(f"O título ({filme}) é um filme Muito Bom!")
elif nota == 3:
    print(f"O título ({filme}) é um filme Bom!")
elif nota == 2:
    print(f"O título ({filme}) é um filme Regular.")
elif nota == 1:
    print(f"O título ({filme}) é um filme Ruim.")