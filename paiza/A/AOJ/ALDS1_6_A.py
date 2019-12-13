def CountingSort(A, B, k):
    global n
    C = [0 for _ in range(k)]

    # C[i] に i の出現数を記録する
    for j in range(n):
        C[A[j]] += 1

    # C[i] に i 以下の数の出現数を記録する
    for i in range(1, k):
        C[i] = C[i] + C[i-1]

    for j in range(n-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1

    print(*B)


n = int(input())
A = list(map(int, input().split()))
B = [0 for _ in range(n)]
k = max(A)+1
CountingSort(A, B, k)
