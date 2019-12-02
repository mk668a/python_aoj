def merge(A, left, mid, right):
    A_l = A[left:mid]
    A_r = A[mid:right]
    f_inf = float('inf')
    A_l.append(f_inf)
    A_r.append(f_inf)
    global c
    # print(A_l)
    # print(A_r)
    # print("go")
    l, r = 0, 0
    for i in range(left, right):
        c += 1
        if A_l[l] < A_r[r]:
            A[i] = A_l[l]
            l += 1
            # print("A_l[l] < A_r[r]", A)
        else:
            A[i] = A_r[r]
            r += 1
            # print("else", A)
    # print(A)
    # print()


def mergeSort(A, left, right):
    if left + 1 < right:
        mid = int((left+right)/2)
        # print("l =", left, "mid =", mid, "r =", right)
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)


n = int(input())
A = list(map(int, input().split()))
c = 0

mergeSort(A, 0, len(A))
print(*A)
print(c)
