# Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
# S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?
# Entrada
# Não há nenhuma entrada neste problema.
# Saída
# A saída contém um valor correspondente ao valor de S.
# O valor deve ser impresso com dois dígitos após o ponto decimal.

s = 1
passo = 3
passo2 = 2
while passo <= 39:    
    s += passo/passo2
    passo += 2    
    passo2 *= 2
print(f"{s:.2f}")