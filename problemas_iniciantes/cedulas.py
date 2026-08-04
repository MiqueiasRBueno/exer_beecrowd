# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser
# decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre
# o valor lido e a relação de notas necessárias.
# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).
# Saída
# Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo
# fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a
# mensagem: “Presentation Error”.

N = int(input())
valor_notas_divisores = [100, 50, 20, 10, 5, 2, 1]
resto = N
quantidade_notas = []
for divisior in valor_notas_divisores:
    quantidade = resto // divisior
    resto %= divisior
    quantidade_notas.append(quantidade)
print(N)
cont = 0
for quantidade_cedulas in quantidade_notas: 
    print(f"{quantidade_cedulas} nota(s) de R$ {valor_notas_divisores[cont]:.2f}")
    cont += 1
