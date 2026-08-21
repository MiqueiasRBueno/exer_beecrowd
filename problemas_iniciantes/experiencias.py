# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar
# os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano,
# quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.
# Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos.
# Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados,
# o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.
# Entrada
# A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir.
# Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas
# e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).
# Saída
# Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma
# em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.

numero_entradas = int(input())
coelho = rato = sapo = total_especie = 0
for v in range(0, numero_entradas):
    quantidade_especie, especie_teste = map(str, input().split())
    if str(especie_teste).lower() == "c":
        coelho += int(quantidade_especie)
        total_especie += int(quantidade_especie)
    elif str(especie_teste).lower() == "r":
        rato += int(quantidade_especie)
        total_especie += int(quantidade_especie)
    elif str(especie_teste).lower() == "s":
        sapo += int(quantidade_especie)
        total_especie += int(quantidade_especie)
print(f"Total: {total_especie} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print(f"Percentual de coelhos: {(coelho * 100) / total_especie:.2f} %")
print(f"Percentual de ratos: {(rato * 100) / total_especie:.2f} %")
print(f"Percentual de sapos: {(sapo * 100) / total_especie:.2f} %")
