# Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo
# resto da divisão dele por 5 for igual a 2 ou igual a 3.
# Entrada
# O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.
# Saída
# Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

valor_x = int(input())
valor_y = int(input())
for v_x_y in range(min(valor_x, valor_y) + 1, max(valor_x, valor_y)):
    if v_x_y % 5 == 2 or v_x_y % 5 ==3:
        print(v_x_y)
        