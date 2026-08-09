# Leia um número inteiro que representa um código de DDD para discagem interurbana. 
# Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:
#           DDD |   Destino
#           61  | Brasilia
#           71  | Salvador
#           11  | São Paulo
#           21  | Rio de Janeiro
#           32  | Juiz de Fora
#           19  | Campinas
#           27  | Vitoria
#           31  | Belo Horizonte
# Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
# DDD nao cadastrado
# Entrada
# A entrada consiste de um único valor inteiro.
# Saída
# Imprima o nome da cidade correspondente ao DDD existente na entrada. 
# Imprima DDD nao cadastrado caso não existir DDD correspondente ao número digitado.

ddd_cidades = {61: "Brasilia", 71 : "Salvador", 11 : "Sao Paulo", 21 : "Rio de Janeiro", 32 : "Juiz de Fora",
               19 : "Campinas", 27 : "Vitoria", 31 : "Belo Horizonte"}
codigo_ddd = int(input())
if codigo_ddd in ddd_cidades: print(ddd_cidades[codigo_ddd])
else: print("DDD nao cadastrado")