import random


def countK(P, K):
    zero, one = 0, 0
    notRand = False
    for num in P:
        if num == "0":
            zero += 1
            one = 0
        else:
            zero = 0
            one += 1
        # print('zero', zero, "one", one, "num", num, "p:", p)
        if (one == K) or (zero == K):
            notRand = True
            break
    return notRand


N, K = (int(x)for x in input().split())

count = 0
x = bin(0)
for i in range(2**N):
    p = str(x[2:]).zfill(N)
    # print(p)
    if(not countK(p, K)):
        count += 1
    x = int(x, 2)
    x = bin(x + 1)

print(count / 2**N)
