# Escreva um programa que leia um valor inteiro N.
# Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.
# Entrada
# O arquivo de entrada contém um número inteiro positivo N.
# Saída
# Imprima a saída conforme o exemplo fornecido.

num_linhas = int(input())
cont = x = 0
while cont < num_linhas:
    for pum in range(1, 4):
        x += 1
        print(x, end=" ")
    print("PUM")
    x += 1
    cont += 1