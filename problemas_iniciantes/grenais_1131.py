# A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado
# de vários GRENAIS. Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL.
# Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1,
# o algoritmo deve ser executado novamente solicitando o número de gols marcados pelos
# times em uma nova partida, caso contrário deve ser encerrado imprimindo:
# - Quantos GRENAIS fizeram parte da estatística.
# - O número de vitórias do Inter.
# - O número de vitórias do Grêmio.
# - O número de Empates.
# - Uma mensagem indicando qual o time que venceu o maior número de
# GRENAIS (ou "Nao houve vencedor", caso termine empatado).
# Entrada
# O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter
# e pelo Grêmio respectivamente. Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.
# Saída
# Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)".
# Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição apresentada acima.
# Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.

num_grenais = vit_inter = vit_gremio = empate_times = 0
while True:
    gols_inter, gols_gremio = map(int, input().split())
    num_grenais += 1
    empate_times += gols_inter == gols_gremio
    vit_inter += gols_inter > gols_gremio
    vit_gremio += gols_inter < gols_gremio
    print("Novo grenal (1-sim 2-nao)")
    novo_grenal = [1, 2]
    while novo_grenal != 1 and novo_grenal != 2:
        novo_grenal = int(input())
    if novo_grenal == 2:
        break
print(f"{num_grenais} grenais")
print(f"Inter:{vit_inter}")
print(f"Gremio:{vit_gremio}")
print(f"Empates:{empate_times}")
if vit_inter == vit_gremio: print("Nao houve vencedor")
else:
    if vit_inter > vit_gremio: time_vencedor = "Inter"
    else: time_vencedor = "Gremio"
    print(f"{time_vencedor} venceu mais")