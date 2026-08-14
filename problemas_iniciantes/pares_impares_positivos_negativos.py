# Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares,
# quantos valores digitados foram ímpares,
# quantos valores digitados foram positivos e quantos valores digitados foram negativos.
# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.
# Saída
# Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha,
# não esquecendo o final de linha após cada uma.

cont_pares = []
cont_impares = []
cont_positivos = []
cont_negativos = []
for num in range(0, 5):
    num_inteiros = int(input())
    if num_inteiros % 2 == 0:
        cont_pares.append(num_inteiros)
    else:
        cont_impares.append(num_inteiros)
    if num_inteiros < 0:
        cont_negativos.append(num_inteiros)
    elif num_inteiros > 0:
        cont_positivos.append(num_inteiros)
print(f"{len(cont_pares)} valor(es) par(es)")
print(f"{len(cont_impares)} valor(es) impar(es)")
print(f"{len(cont_positivos)} valor(es) positivo(s)")
print(f"{len(cont_negativos)} valor(es) negativo(s)")
