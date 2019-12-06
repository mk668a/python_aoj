def merge(A, left, mid, right):
    A_l = A[left:mid]
    A_r = A[mid:right]
    f_inf = float('inf')
    A_l.append(f_inf)
    A_r.append(f_inf)
    l, r = 0, 0
    global c
    for i in range(left, right):
        if A_l[l] < A_r[r]:
            A[i] = A_l[l]
            l += 1
            c += r
        else:
            A[i] = A_r[r]
            r += 1


def mergeSort(A, left, right):
    if left + 1 < right:
        mid = int((left+right)/2)
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)


n = int(input())
A = list(map(int, input().split()))
c = 0

mergeSort(A, 0, len(A))
print(c)
