# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir.
# Cada caso de teste consiste de dois inteiros X e Y.
# Você deve apresentar a soma de todos os ímpares existentes entre X e Y.
# Entrada
# A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir.
# Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.
# Saída
# Imprima a soma de todos valores ímpares entre X e Y.

quantidade_casos_teste = int(input())
x = 0
lista_resultado = []
while True:
    numero_x, numero_y = map(int, input().split())
    maior = menor = numero_x
    if numero_y > maior:
        maior = numero_y
    if numero_y < menor:
        menor = numero_y
    soma = 0
    for v in range(menor + 1, maior):
        if v % 2 != 0:
            soma += v
    lista_resultado.append(soma)
    x += 1
    if x >= quantidade_casos_teste:
        break
for s in lista_resultado:
    print(s)