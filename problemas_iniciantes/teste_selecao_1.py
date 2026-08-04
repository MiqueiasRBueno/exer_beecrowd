# Leia 4 valores inteiros A, B, C e D.
# A seguir, se B for maior do que C e se D for maior do que A,
# e a soma de C com D for maior que a soma de A e B e se C e D, ambos,
# forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".
# Entrada
# Quatro números inteiros A, B, C e D.
# Saída
# Mostre a respectiva mensagem após a validação dos valores.

a, b, c, d = map(int, input().split())
e_par = a % 2 ==0
positivo = c > 0 and d > 0
soma = (c + d) > (a + b)
b_maior_c = b > c
d_maior_a = d > a
if e_par and positivo and soma and b_maior_c and d_maior_a: print("Valores aceitos")
else: print("Valores nao aceitos")
