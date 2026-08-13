# Pedrinho está organizando um evento em sua Universidade.
# O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês.
# O problema é que Pedrinho quer calcular o tempo que o evento vai durar,
# uma vez que ele sabe quando inicia e quando termina o evento.
# Sabendo que o evento pode durar de poucos segundos a vários dias,
# você deverá ajudar Pedrinho a calcular a duração deste evento.
# Entrada
# Como entrada, na primeira linha vai haver a descrição “Dia”,
# seguido de um espaço e o dia do mês no qual o evento vai começar.
# Na linha seguinte, será informado o momento no qual o evento vai iniciar,
# no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra
# informação no mesmo formato das duas primeiras linhas, indicando o término do evento.
# Saída
# Na saída, deve ser apresentada a duração do evento, no seguinte formato:
# W dia(s)
# X hora(s)
# Y minuto(s)
# Z segundo(s)
# Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

dia_ini = int(input().split()[1])
hr_ini, min_ini, seg_ini = map(int, input().split(" : "))
dia_final = int(input().split()[1])
hr_final, min_final, seg_final = map(int, input().split(" : "))
dia_seg_ini = dia_ini * 86400
hr_seg_ini = hr_ini * 3600
min_seg_ini = min_ini * 60
dia_seg_final = dia_final * 86400
hr_seg_final = hr_final * 3600
min_seg_final = min_final * 60
seg_ini_total = dia_seg_ini + hr_seg_ini + min_seg_ini + seg_ini
seg_final_total =  dia_seg_final + hr_seg_final + min_seg_final + seg_final
seg_diferenca_total = seg_final_total - seg_ini_total
dia_total = seg_diferenca_total // 86400
hr_total = seg_diferenca_total % 86400 // 3600
min_total = (seg_diferenca_total % 86400 % 3600) // 60
seg_total = seg_diferenca_total % 86400 % 3600 % 60
print(f"{dia_total} dia(s)")
print(f"{hr_total} hora(s)")
print(f"{min_total} minuto(s)")
print(f"{seg_total} segundo(s)")
