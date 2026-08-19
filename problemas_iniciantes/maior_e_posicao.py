# Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.
# Entrada
# O arquivo de entrada contém 100 números inteiros, positivos e distintos.
# Saída
# Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

cem_inteiros = []
for v in range(0,100):
    cem_inteiros.append(int(input()))
print(max(cem_inteiros))
print(cem_inteiros.index(max(cem_inteiros)) + 1)
