M, N, K = (int(x) for x in input().split())
a = [0 for _ in range(K)]

for i in range(K):
    r = int(input()) - 1
    for j in range(len(a)):
        if r == j:
            if N > 0:
                N -= 1
                a[r] += 1
        else:
            if a[j] > 0:
                a[j] -= 1
                a[r] += 1

max_v = 0
for i in range(len(a)):
    if a[i] >= max_v:
        max_v = a[i]
for i in range(len(a)):
    if a[i] == max_v:
        print(i+1)
