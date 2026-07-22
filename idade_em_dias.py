# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
# Obs.: apenas para facilitar o cálculo, considere ano com 365 dias e o mês com 30 dias.
#  Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364.
#  Este é apenas um exercício com objetivo de testar raciocínio matemático simples.#
# Entrada
# O arquivo de entrada contém um valor inteiro.
# Saída
# Imprima a saída conforme exemplo fornecido.

dias = int(input())
resto = dias
divisores = [365, 30]
id_dias = []
for divisor in divisores:
    idade = resto // divisor
    resto %= divisor
    id_dias.append(idade)
id_dias.append(resto)
ano, mes , dia = id_dias
print(f"""{ano} ano(s)
{mes} mes(es)
{dia} dia(s)""")
