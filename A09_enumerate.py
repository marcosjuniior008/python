# ENUMERATE

for indice in "Ciencia de Dados":
    print(f"{indice}")

for indice in enumerate("ciencia de dados"):
    print(f"{indice}")

for indice, caractere in enumerate("ciencia de dados"):
    print(f"{indice}): {caractere}")

lista = ["Brasil", "EUA", "inglaterra", "italia", "frança", "Alemanha"]
for indice, country in enumerate(lista):
    print(f"{indice} - {country}")

print()
for indice, country in enumerate(lista, start=3):
    print(f"{indice} - {country}")


