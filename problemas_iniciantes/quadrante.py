# Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano.
# Para cada ponto escrever o quadrante a que ele pertence.
# O algoritmo será encerrado quando pelo menos uma de duas coordenadas
# for NULA (nesta situação sem escrever mensagem alguma).
# Entrada
# A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.
# Saída
# Para cada caso de teste mostre em qual quadrante do sistema
# cartesiano se encontra a coordenada lida, conforme o exemplo.

# Inicia um laço de repetição infinito (roda até encontrar o 'break')
while True:
    # Recebe a entrada do usuário, divide pelos espaços e converte os valores para float
    x, y = map(float, input().split())

    # Verifica se alguma das coordenadas é igual a zero para encerrar o programa
    if x == 0 or y == 0:
        break

    # Se nenhuma for zero, entra nas verificações dos quadrantes
    else:
        # Verifica a primeira condição original (X positivo e Y maior que zero)
        if x > 0 < y:
            print("primeiro")

            # Verifica a segunda condição original (X positivo e Y menor que zero)
        elif x > 0 > y:
            print("quarto")

            # Verifica a terceira condição original (X negativo e Y menor que zero)
        elif x < 0 > y:
            print("terceiro")

            # Se não caiu em nenhuma das anteriores, assume o segundo quadrante
        else:
            print("segundo")
