# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
# Entrada
# Quatro números inteiros representando a hora de início e fim do jogo.
# Saída
# Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

hora_inicio, minutos_inicio, hora_fim, minutos_fim = map(int, input().split())
inicio_total = hora_inicio * 60 + minutos_inicio
fim_total = hora_fim * 60 + minutos_fim
if fim_total > inicio_total: duracao_total = fim_total - inicio_total
else: duracao_total = (1440 + fim_total ) - inicio_total
tempo_jogo_horas = duracao_total // 60
tempo_jogo_minutos = duracao_total % 60
print(f"O JOGO DUROU {tempo_jogo_horas} HORA(S) E {tempo_jogo_minutos} MINUTO(S)")
