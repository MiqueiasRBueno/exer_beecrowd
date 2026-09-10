# Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. 
# O último dado, que não entrará nos cálculos, contém o valor de idade negativa. 
# Calcular e imprimir a idade média deste grupo de indivíduos.
# Entrada
# A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.
# Saída
# A saída contém um valor correspondente à média de idade dos indivíduos.
# A média deve ser impressa com dois dígitos após o ponto decimal.

total_idade = cont = 0
while True:
    idade_individuos = int(input())
    if idade_individuos < 0:
        break
    total_idade += idade_individuos
    cont += 1
if cont > 0:
    print(f"{total_idade / cont:.2f}")