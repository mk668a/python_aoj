import random

M, N = (int(x) for x in input().split())

add, sub = [], []

for i in range(M):
    r1 = random.randint(0, 99)
    while 1:
        r2 = random.randint(0, 99-r1)
        if ([r1, r2] not in add):
            add.append([r1, r2])
            break

for i in range(N):
    r1 = random.randint(0, 99)
    while 1:
        r2 = random.randint(0, r1)
        if ([r1, r2] not in sub):
            sub.append([r1, r2])
            break

for a in add:
    print(a[0], "+", a[1], "=")

for s in sub:
    print(s[0], "-", s[1], "=")
