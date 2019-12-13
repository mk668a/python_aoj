import random

M, N = (int(x) for x in input().split())

add, sub = [], []

r1 = 0
r2 = 0
for i in range(M):
    if r2 > 99 - r1:
        r1 += 1
        r2 = 0
    add.append([r1, r2])
    r2 += 1

r1 = 0
r2 = 0
for i in range(N):
    if r1 > 99:
        r2 += 1
        r1 = r2
    sub.append([r1, r2])
    r1 += 1

for a in add:
    print(a[0], "+", a[1], "=")

for s in sub:
    print(s[0], "-", s[1], "=")
