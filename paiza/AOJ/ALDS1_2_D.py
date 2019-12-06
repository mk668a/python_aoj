def insertionSort(A, n, g):
    global cnt
    for i in range(n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            cnt = cnt + 1
        A[j + g] = v


def shellSort(A, n):
    global cnt
    global m
    global G
    for i in range(m):
        insertionSort(A, n, G[i])


cnt = 0
n = int(input())
A = []
G = []
i = 1
while i <= n:
    G.append(i)
    i = 3 * i + 1
G.reverse()
m = len(G)
for i in range(n):
    A.append(int(input()))
shellSort(A, n)
print(m)
print(*G)
print(cnt)
for i in range(n):
    print(A[i])
