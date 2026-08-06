# A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:
# Salário	Percentual de Reajuste
# 0 - 400.00            15%
# 400.01 - 800.00       12%
# 800.01 - 1200.00      10%
# 1200.01 - 2000.00     7%
# Acima de 2000.00      4%
# Leia o salário do funcionário e calcule e mostre o novo salário, 
# bem como o valor de reajuste ganho e o índice reajustado, em percentual.
# Entrada
# A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.
# Saída
# Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste 
# (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

salario_atual_funcionario = float(input())
if salario_atual_funcionario <= 400: percentual = 15
elif 400 < salario_atual_funcionario <= 800: percentual = 12
elif 800 < salario_atual_funcionario <= 1200: percentual = 10
elif 1200 <salario_atual_funcionario <= 2000: percentual = 7
else: percentual = 4
reajuste = salario_atual_funcionario * (percentual / 100)
print(f'Novo salario: {salario_atual_funcionario + reajuste:.2f}')
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
