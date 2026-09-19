tamanho_sequencia = int(input())
divisores = []
x = 3
while len(divisores) < tamanho_sequencia:
    divisores.append(x)
    x += 2
for v in divisores:
    print(v, end=" ")