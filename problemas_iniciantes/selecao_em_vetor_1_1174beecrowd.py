# Faça um programa que leia um vetor A[100]. No final,
# mostre todas as posições do vetor que armazenam um valor menor ou igual a 10
# e o valor armazenado em cada uma das posições.
# Entrada
# A entrada contém 100 valores, podendo ser inteiros, reais, positivos ou negativos.
# Saída
# Para cada valor do vetor menor ou igual a 10, escreva "A[i] = x",
# onde i é a posição do vetor e x é o valor armazenado na posição, com uma casa após o ponto decimal.

lista_valores = []
valor_str = []
for ent_valor in range(0, 100):
    lista_valores.append(float(input()))
    valor_str = lista_valores[:]
lista_valores.clear()
for pos, valor in enumerate(valor_str):
    valor_mostra = float(valor)
    if valor_mostra <= 10: print(f'A[{pos}] = {valor_mostra}')
