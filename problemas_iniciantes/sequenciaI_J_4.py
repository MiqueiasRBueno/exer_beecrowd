#Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.
# Entrada
# Não há nenhuma entrada neste problema.
# Saída
# Imprima a sequencia conforme exemplo abaixo.

# Inicializa a variável 'i' com o valor 0 (ponto de partida do laço)
i = 0

# Executa o bloco enquanto 'i' for menor ou igual a 20
while i <= 20:

    # Laço interno: gera valores para 'j' de 1 até 3 (o 4 é exclusivo)
    for j in range(1, 4):

        # Verifica se 'i' é divisível por 10 (múltiplos como 0, 10 e 20)
        if i % 10 == 0:
            # Exibe os números como inteiros (sem casas decimais)
            print(f'I={int(i / 10)} J={int(j + i / 10)}')

            # Caso 'i' não seja múltiplo de 10 (valores com decimais)
        else:
            # Exibe os números como decimais, limitados a 1 casa após a vírgula (:.1f)
            print(f'I={i / 10:.1f} J={j + i / 10:.1f}')

            # Incrementa 'i' em 2 unidades para avançar no laço 'while'
    i += 2
