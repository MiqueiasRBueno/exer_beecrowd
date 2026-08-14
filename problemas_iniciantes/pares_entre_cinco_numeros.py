# Faça um programa que leia 5 valores inteiros.
# Conte quantos destes valores digitados são pares e mostre esta informação.
# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.
# Saída
# Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

num_pares = cont = 0
for num in range(0, 5):
    num_pares = int(input())
    if num_pares % 2 == 0:
        cont += 1
print(f"{cont} valores pares")
