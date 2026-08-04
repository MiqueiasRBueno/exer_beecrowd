# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
# A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
# As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
# A seguir mostre a relação de notas necessárias.
# Entrada
# O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
# Saída
# Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.
# Obs: Utilize ponto (.) para separar a parte decimal.

valor = round(float(input()), 2)
valor_restante = valor * 100
valor_moeda_divisores = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
total_notas = []
total_moedas = []
for d in valor_moeda_divisores:
    divisor = d * 100
    quant_not_moedas = valor_restante // divisor
    valor_restante %= divisor
    if divisor > 100: total_notas.append(quant_not_moedas)
    else: total_moedas.append(quant_not_moedas)
print("NOTAS:")
cont_n = 0
for nota in total_notas:
    print(f"{int(nota)} nota(s) de R$ {valor_moeda_divisores[cont_n]:.2f}")
    cont_n += 1
print("MOEDAS:")
cont_m = 6
for moeda in total_moedas:
    print(f"{int(moeda)} moeda(s) de R$ {valor_moeda_divisores[cont_m]:.2f}")
    cont_m += 1
