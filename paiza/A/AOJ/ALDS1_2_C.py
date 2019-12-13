def BubbleSort(C, N):
    for i in range(N):
        for j in reversed(range(i + 1, N)):
            if C[j][1:] < C[j - 1][1:]:
                a = C[j]
                C[j] = C[j - 1]
                C[j - 1] = a
    return C


def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j][1:] < C[minj][1:]:
                minj = j
        a = C[i]
        C[i] = C[minj]
        C[minj] = a
    return C


N = int(input())
C = list(input().split())
C2 = C[:]
a = BubbleSort(C, N)
b = SelectionSort(C2, N)
print(*a)
print('Stable')
print(*b)
if a == b:
    print('Stable')
else:
    print('Not stable')
