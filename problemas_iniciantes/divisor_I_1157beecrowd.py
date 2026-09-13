# Ler um número inteiro N e calcular todos os seus divisores.
# Entrada
# O arquivo de entrada contém um valor inteiro.
# Saída
# Escreva todos os divisores positivos de N, um valor por linha.

num_int_N = int(input())
for valor in range(1, num_int_N + 1):
    if num_int_N % valor == 0:
        print(valor)