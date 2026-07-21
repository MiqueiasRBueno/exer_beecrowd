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
n100 = N // 100
n50 = (N % 100) // 50
n20 = (N % 100 % 50) // 20
n10 = (N % 100 % 50 % 20) // 10
n5 = (N % 100 % 50 % 20 % 10) // 5
n2 = (N % 100 % 50 % 20 % 10 % 5) // 2
n1 = (N % 100 % 50 % 20 % 10 % 5 % 2) // 1
print(N)
print(f"{n100} nota(s) de R$ 100,00")
print(f"{n50} nota(s) de R$ 50,00")
print(f'{n20} nota(s) de R$ 20,00')
print(f"{n10} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n2} nota(s) de R$ 2,00")
print(f"{n1} nota(s) de R$ 1,00")
