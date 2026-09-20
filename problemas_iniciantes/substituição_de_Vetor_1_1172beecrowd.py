# Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1.
# Em seguida mostre o vetor X.
# Entrada
# A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.
# Saída
# Para cada posição do vetor, escreva "X[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.

lista_vetores = []
vetor_x = 0
for num_entradas in range(0, 10):
    num_x = int(input())
    if num_x < 1:
        vetor_x = 1
    else: vetor_x = num_x
    lista_vetores.append(str(vetor_x))
for pos, v in enumerate(lista_vetores):
    print(f'X[{pos}] = {v}')
