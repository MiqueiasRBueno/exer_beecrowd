# Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo.
# Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.
# Entrada
# A entrada contém um número inteiro N.
# Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.
# Saída
# Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal,
# ou “divisao impossivel” caso não seja possível efetuar o cálculo.
# Obs.: Cuide que a divisão entre dois inteiros em algumas linguagens como o C e C++ gera outro inteiro. Utilize cast :)

# Lê a quantidade de casos de teste que o programa executará
numero_de_teste = int(input())

# Cria um laço de repetição que vai rodar o código de "0" até o "numero_de_teste - 1"
for numt in range(0, numero_de_teste):

    # O 'try' (tentar) inicia um bloco onde monitoramos possíveis erros que fariam o programa travar
    try:
        # Lê dois números inteiros na mesma linha (dividendo e divisor) separados por espaço
        dividendo, divisor = map(int, input().split())

        # Realiza a divisão e exibe o resultado formatado com exatamente 1 casa decimal (.1f)
        print(f'{dividendo / divisor:.1f}')

    # O 'except' captura especificamente o erro de tentar dividir um número por zero (ZeroDivisionError)
    except ZeroDivisionError:
        # Em vez de fechar o programa com um erro, ele exibe esta mensagem amigável e continua o laço
        print("divisao impossivel")
