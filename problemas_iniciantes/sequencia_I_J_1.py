# Você deve fazer um programa que apresente a sequência conforme o exemplo abaixo.
# Entrada
# Não há nenhuma entrada neste problema.
# Saída
# Imprima a sequência conforme exemplo abaixo.

i = 1
j = 60
while True:
    print(f"I={i} J={j}")
    i += 3
    j -= 5
    if j < 0:
        break
        