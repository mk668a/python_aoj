from random import random as rand


def PI(n):
    inCircle = 0
    for i in range(n):
        x = rand()
        y = rand()
        d = (x - 0.5)**2 + (y - 0.5)**2
        if d < 0.25:
            inCircle = inCircle + 1
    return 4 * inCircle / n


n = 1
for i in range(1, 6):
    n *= 10
    print("n =", n)
    print(PI(n), end='\n\n')
