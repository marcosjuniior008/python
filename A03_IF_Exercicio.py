# faça uma rotina com uso do if, elif, else quer receba um valor numerico inteiro

acordei = True
if acordei:
    print("acordei cedo")
else:
    print("faltei na escola")

if acordei:
     print("me arrumei e fui ao colegio")
else:
    print("não fui ao colegio e tomei bronca")

    idade = int(input("Digite a idade"))
if idade >=60:
    print("Voto é opcional")
elif idade >= 18:
    print("Voto é obrigatótio")
elif idade >= 16:
    print("Voto opcional")
else:
    print("não pode votar")

print("Acabou")

if idade >= 60 or idade <= 16 and idade >= 16:
    print("O Voto é Opcional")
