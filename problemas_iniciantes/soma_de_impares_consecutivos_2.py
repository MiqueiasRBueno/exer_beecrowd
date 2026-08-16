# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.
# Entrada
# O arquivo de entrada contém dois valores inteiros.
# Saída
# O programa deve imprimir um valor inteiro. Este valor é a soma dos valores
# ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

x = int(input())
y =  int(input())
menor = maior = x
if y > maior:
    maior = y
if y < menor:
    menor = y
soma_impares = 0
for v in range(menor + 1, maior):
    if v % 2 != 0:
        soma_impares += v
print(soma_impares)
