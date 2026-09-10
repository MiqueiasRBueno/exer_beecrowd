# Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.
# Entrada
# A entrada contém um valor inteiro N (0 < N < 13).
# Saída
# A saída contém um valor inteiro, correspondente ao fatorial de N.

valor_fatorial = int(input())
if valor_fatorial <= 1:
    print(1)
else:
    fatorial = valor_fatorial
    for valor in range(1, valor_fatorial):
        fatorial *= valor
    print(fatorial)
