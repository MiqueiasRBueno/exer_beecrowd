# Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos
# números que não são múltiplos de 13 entre X e Y, incluindo ambos.
# Entrada
# O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.
# Saída
# Imprima a soma de todos os valores não divisíveis por 13 entre
# os dois valores lidos na entrada, inclusive ambos se for o caso.

numero_int_x = int(input())
numero_int_y = int(input())
soma = 0
for num_x_y in range(min(numero_int_x, numero_int_y), max(numero_int_x, numero_int_y) + 1):
    if num_x_y % 13 != 0:
        soma += num_x_y
print(soma)