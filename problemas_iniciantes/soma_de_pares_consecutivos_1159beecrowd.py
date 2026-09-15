# O programa deve ler um valor inteiro X indefinidas vezes.
# (O programa irá parar quando o valor de X for igual a 0). Para cada X lido, imprima a soma dos 5
# pares consecutivos a partir de X, inclusive o X , se for par. Se o valor de entrada for 4,
# por exemplo, a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12,
# enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a soma de 12+14+16+18+20.
# Entrada
# O arquivo de entrada contém muitos valores inteiros. O último valor do arquivo é zero.
# Saída
# Imprima a saida conforme a explicação acima e o exemplo abaixo.

while True:
    entrada_x = int(input())
    if entrada_x == 0:
        break
    else:
        if entrada_x % 2 == 0:
            inicio = entrada_x
        else:
            inicio = entrada_x + 1
        soma = inicio
        aux = inicio + 2
        for _ in range(0, 4):
            soma += aux
            aux += 2
        print(soma)

