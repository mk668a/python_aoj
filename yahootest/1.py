A = list(map(int, input().split()))
B = []
for a in A:
    if a != 0 and a not in B:
        B.append(a)
print(*B)
