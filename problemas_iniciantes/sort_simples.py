# Leia 3 valores inteiros e ordene-os em ordem crescente. 
# No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.
# Entrada
# A entrada contem três números inteiros.
# Saída
# Imprima a saída conforme foi especificado.

int1, int2, int3 = map(int, input().split())
ordem_crescente = [int1, int2, int3]
ordem_crescente.sort()
for valor in ordem_crescente:
    print(valor)
print()
for v in (int1, int2, int3):
    print(v)
