# Faça um algoritmo para ler um valor A e um valor N.
# Imprimir a soma de A + i para cada i com os valores (0 <= i <= N-1). Enquanto N for negativo ou ZERO,
# um novo N(apenas N) deve ser lido.
# Entrada
# A entrada contém somente valores inteiros, podendo ser positivos ou negativos. Todos os valores estão na mesma linha.
# Saída
# A saída contém apenas um valor inteiro.

# Lê a linha inteira e transforma tudo em uma lista de inteiros
valores = list(map(int, input().split()))

# O primeiro valor sempre será o A
A = valores[0]

# Procuramos o primeiro valor positivo a partir do segundo elemento para ser o N
for valor in valores[1:]:
    if valor > 0:
        N = valor
        break  # Achou o N válido? Para o laço!

# Agora é só fazer a lógica da soma...
print(N)
