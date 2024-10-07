# lista = conjunto de valores
# lista = [valor1 , valor2 ...]
# lista = list(valor1, valor2, ...)

listaVazia = [] # cria lista vazia

listaComeElementos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listaComeElementos = [7, "Python", 3.14159, True, 'C']

listaComeElementos[0]  # pega o primeiro elemento
listaComeElementos[-1] # pega o ultimo elemento
listaComeElementos[:4] # pega os 3 primeiros elementos
listaComeElementos[3:] # pega do terceiro item em diante
listaComeElementos[3:6] # pega do terceiro ate o quinto
listaComeElementos[3:8:2] # pega do terceiro ao sétimo de 2 em 2

print(listaComeElementos[3:8:2])

len(listaComeElementos[3:8:2])

len(listaComeElementos) # retorna numero de elementos
print(len(listaComeElementos))

max(listaComeElementos) # retorna o maior valor
print(max(listaComeElementos))

min(listaComeElementos) # retorna o menor valor
sum(listaComeElementos) # retorna a soma de todos os elementos

print(sum(listaComeElementos))
sorted(listaComeElementos) # retorna a lita em ordem crescente

listaVazia.append(1) # adiciona um elemento
listaVazia.append("texto")
listaVazia.append(true)

listaVazia.insert(2,"Novo elemento") #adiciona elemento no indicie 2
print(listaVazia)

listaVazia.remove("texto") # remove o primeiro elemento encontrado
print(listaVazia)

print(listaVazia.pop(0))
print(listaVazia)
      
print(listaVazia.index("Novo elemento"))



