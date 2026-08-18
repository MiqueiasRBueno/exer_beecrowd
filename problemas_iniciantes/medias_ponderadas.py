# Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir.
# Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal.
# Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2,
# o segundo valor tem peso 3 e o terceiro valor tem peso 5.
# Entrada
# O arquivo de entrada contém um valor inteiro N na primeira linha.
# Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor.
# Saída
# Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo.

# 1. Lê a quantidade de casos de teste (quantas linhas de notas serão digitadas)
n = int(input())

# Cria uma lista vazia para armazenar os resultados formatados de cada cálculo
media_ponderada = []

# 2. Laço de repetição que vai rodar exatamente 'n' vezes (uma para cada caso)
for valor in range(0, n):
    # Captura uma linha com 3 notas separadas por espaço, converte-as para decimal (float)
    # e distribui os valores simultaneamente nas três variáveis
    media_1, media_2, media_3 = map(float, input().split())

    # Calcula a média ponderada: multiplica cada nota por seu respectivo peso (2, 3 e 5)
    # e divide a soma de tudo pela soma dos pesos (2 + 3 + 5 = 10)
    media = ((media_1 * 2) + (media_2 * 3) + (media_3 * 5)) / 10

    # Formata o resultado para ter apenas 1 casa decimal (:.1f)
    # e adiciona o texto formatado no final da lista criada anteriormente
    media_ponderada.append(f"{media:.1f}")

# 3. Laço de repetição final para exibir os resultados armazenados
for v in media_ponderada:
    print(v)  # Imprime uma média por linha, exatamente na ordem em que foram calculadas
