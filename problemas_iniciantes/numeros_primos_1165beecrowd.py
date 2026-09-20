# Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo.
# Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.
# Entrada
# A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100),
# indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes
# contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.
# Saída
# Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”,
# de acordo com a especificação fornecida.

numero_testes = int(input())
for _ in range(numero_testes):
    numero_primo = int(input())
    dividendo = numero_primo
    primo = True
    if dividendo <= 1: primo = False
    elif dividendo <= 3: primo = True
    elif dividendo % 2 == 0: primo = False
    else:
        for num in range(3, int(numero_primo ** 0.5) + 1, 2):
            if dividendo % num == 0:
                primo = False
                break
    if primo: print(f"{numero_primo} eh primo")
    else: print(f"{numero_primo} nao eh primo")