# Na matemática, um número perfeito é um número inteiro para o qual a soma de todos os seus divisores positivos
# próprios (excluindo ele mesmo) é igual ao próprio número. Por exemplo o número 6 é perfeito, pois 1+2+3 é igual a 6.
# Sua tarefa é escrever um programa que imprima se um determinado número é perfeito ou não.
# Entrada
# A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 20),
# indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes
# contém um valor inteiro X (1 ≤ X ≤ 108), que pode ser ou não, um número perfeito.
# Saída
# Para cada caso de teste de entrada, imprima a mensagem “X eh perfeito” ou “X nao eh perfeito”, de acordo

numeros_testes = int(input())
for testes in range(numeros_testes):
    numero_perfeito = int(input())
    if numero_perfeito == 1:
        print("1 nao eh perfeito")
        continue
    soma = 1
    limite = int(numero_perfeito ** 0.5)
    for valor in range(2, limite + 1):
        if numero_perfeito % valor == 0:
            soma += valor
            outro_divisor = numero_perfeito // valor
            if outro_divisor != valor: soma += outro_divisor
    if soma == numero_perfeito: print(f"{numero_perfeito} eh perfeito")
    else: print(f"{numero_perfeito} nao eh perfeito")
