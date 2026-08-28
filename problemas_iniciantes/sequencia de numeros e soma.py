# Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero).
# Para cada par lido, mostre a sequência do menor até o maior e a
# soma dos inteiros consecutivos entre eles (incluindo o N e M).
# Entrada
# O arquivo de entrada contém um número não determinado de valores M e N.
# A última linha de entrada vai conter um número nulo ou negativo.
# Saída
# Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

while True:
    soma = 0
    m , n = map(int, input().split())
    maior = menor = m
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    if m <= 0 or n <= 0:
        break
    for v in range(menor, maior + 1):
        print(v, end=" ")
        soma += v
    print(f"Sum={soma}")
print()