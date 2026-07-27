# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
# A seguir, calcule e mostre o valor da conta a pagar.
# Entrada
# O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um
# item conforme tabela acima.
# Saída
# O arquivo de saída deve conter a mensagem "Total: R$" seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

codigo_lanche, quantidade_lanche = map(int, input().split())
preco = 0
if codigo_lanche == 1:
    preco = 4
elif codigo_lanche == 2:
    preco = 4.5
elif codigo_lanche == 3:
    preco = 5
elif codigo_lanche == 4:
    preco = 2
elif codigo_lanche == 5:
    preco = 1.5
total_pagar = preco * quantidade_lanche
print(f"Total: R$ {total_pagar:.2f}")
