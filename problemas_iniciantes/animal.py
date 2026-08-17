# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo,
# da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.
# Entrada
# A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o
# animal segundo a figura acima, com todas as letras minúsculas.
# Saída
# Imprima o nome do animal correspondente à entrada fornecida.

classificacao_vertebral = str(input())
classificacao_de_grupo = str(input())
classificacao_alimentacao = str(input())
animal = " "
if classificacao_vertebral == "vertebrado":
    if classificacao_de_grupo == "ave":
        if classificacao_alimentacao == "carnivoro":
            animal = "aguia"
        elif classificacao_alimentacao == "onivoro" :
            animal = "pomba"
    elif classificacao_de_grupo == "mamifero":
        if classificacao_alimentacao == "onivoro":
            animal = "homem"
        elif classificacao_alimentacao == "herbivoro":
            animal = "vaca"
elif classificacao_vertebral == "invertebrado":
    if classificacao_de_grupo == "inseto":
        if classificacao_alimentacao == "hematofago":
            animal = "pulga"
        elif classificacao_alimentacao == "herbivoro":
            animal = "lagarta"
    elif classificacao_de_grupo == "anelideo":
        if classificacao_alimentacao == "hematofago":
            animal = "sanguessuga"
        elif classificacao_alimentacao == "onivoro":
            animal = "minhoca"
print(animal)
