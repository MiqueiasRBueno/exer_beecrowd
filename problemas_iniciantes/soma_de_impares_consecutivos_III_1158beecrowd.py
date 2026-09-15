# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. 
# Cada caso de teste consiste de dois inteiros X e Y. 
# Você deve apresentar a soma de Y ímpares consecutivos a partir de X inclusive o próprio X se ele for ímpar. Por exemplo:
# para a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13
# para a entrada 7 4, a saída deve ser 40, que é equivalente à: 7 + 9 + 11 + 13
# Entrada
# A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. 
# Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.
# Saída
# Imprima a soma dos consecutivos números ímpares a partir do valor X.

quantidade_de_casos_N = int(input())
x = entradas_x = entradas_y = 0
for entradas in range(0, quantidade_de_casos_N):
    entradas_x_y = input().split()
    entradas_x = int(entradas_x_y[0])
    entradas_y = int(entradas_x_y[1])
    if entradas_x % 2 == 0: inicio = entradas_x + 1
    else: inicio = entradas_x
    soma  = passo = inicio
    for total in range(1, entradas_y):      
        passo += 2
        soma += passo
    print(soma)
    