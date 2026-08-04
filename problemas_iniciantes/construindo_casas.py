from math import sqrt
while True:
    try:
        a, b, c = map(int, input().split())
        if a == 0 or b == 0 or c == 0:
            break
        else:
            lado_ter = sqrt(a * b * 100 / c)
            print(int(lado_ter))
    except (EOFError, ValueError):
        break  