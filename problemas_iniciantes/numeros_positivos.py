# Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos
# (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.
# Entrada
# Seis valores, negativos e/ou positivos.
# Saída
# Imprima uma mensagem dizendo quantos valores positivos foram lidos.

cont_numeros_positivos = 0
for c in range(0, 6):
    numeros_positivos = float(input())
    if numeros_positivos > 0:
        cont_numeros_positivos += 1
print(f"{cont_numeros_positivos} valores positivos")