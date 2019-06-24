def merge(a1, a2, a):
    i = 0
    j = 0
    while i < len(a1) or j < len(a2):
        if j >= len(a1) or (i < len(a1) and a1[i] < a2[j]):
            a[i + j] = a1[i]
            i += 1
        else:
            a[i + j] = a2[j]
            j += 1


def mergeSort(a):
    if(len(a) > 1):
        m = int(len(a) / 2)
        n = int(len(a) - m)
        a1 = [0] * m
        a2 = [0] * n
        for i in range(m):
            a1[i] = a[i]
        for i in range(n):
            a2[i] = a[m + i]
        mergeSort(a1)
        mergeSort(a2)
        merge(a1, a2, a)


a = list(map(int, input().split()))
mergeSort(a)
print(*a)
# 5 4 6 1 2 7 3
