# Escreva um programa que leia dois valores X e Y.
# A seguir, mostre uma sequência de 1 até Y, passando para a próxima linha a cada X números.#
# Entrada
# O arquivo de entrada contém dois valores inteiros, (1 < X < 20) e (X < Y < 100000).
#
# Saída
# Cada sequência deve ser impressa em uma linha apenas, com 1 espaço em branco entre
# cada número, conforme exemplo abaixo. Não deve haver espaço em branco após o último valor da linha.

num_por_linha, maior_valor_sequencia = map(int, input().split())
num_imprimir = 1
while num_imprimir < maior_valor_sequencia:
    for v in range(0, num_por_linha):
        print(num_imprimir, end="")
        if v == num_por_linha - 1 or num_imprimir == maior_valor_sequencia:
            print()
            num_imprimir += 1
            break
        else:
            print(end=" ")
        num_imprimir += 1
