num_primo_input = int(input())
limite = num_primo_input
if num_primo_input == 2: print(f'{num_primo_input} eh primo')
elif num_primo_input == 0 or num_primo_input == 1: print(f"{num_primo_input} nao eh primo")

else:
    primo = True
    for divisor in range(1, limite + 1, 2):
        if num_primo_input % divisor == 0:
            primo = False
    if primo:
        print(f"{num_primo_input} é primo")
    else: print(f"{num_primo_input} nao eh primo")