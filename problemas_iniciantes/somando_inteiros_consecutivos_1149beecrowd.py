# Faça um algoritmo para ler um valor A e um valor N.
# Imprimir a soma de A + i para cada i com os valores (0 <= i <= N-1). Enquanto N for negativo ou ZERO,
# um novo N(apenas N) deve ser lido.
# Entrada
# A entrada contém somente valores inteiros, podendo ser positivos ou negativos. Todos os valores estão na mesma linha.
# Saída
# A saída contém apenas um valor inteiro.


entrada = list(map(int, input().split()))
valor_A = entrada[0]
valor_N = 0
for i in range(1, len(entrada)):
    if entrada[i] > 0:
        valor_N = entrada[i]
        break
x = soma = valor_A
for c in range(1, valor_N):
    x += 1
    soma += x
print(soma)