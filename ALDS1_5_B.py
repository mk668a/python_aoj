def merge_sort(A):
    if len(A) <= 1:
        return A
    middle = int(len(A) / 2)
    left = merge_sort(A[:middle])
    right = merge_sort(A[middle:])
    return merge(left, right)


def merge(A, B):
    result = []
    global cnt
    while len(A) > 0 or len(B) > 0:
        cnt += 1
        if len(A) > 0 and len(B) > 0:
            if A[0] <= B[0]:
                result.append(A[0])
                A = A[1:len(A)]
            else:
                result.append(B[0])
                B = B[1:len(B)]
        elif len(A) > 0:
            result.append(A[0])
            A = A[1:len(A)]
        elif len(B) > 0:
            result.append(B[0])
            B = B[1:len(B)]
    return result


if __name__ == '__main__':
    cnt = 0
    n = input()
    A = list(map(int, input().split()))
    print(*merge_sort(A))
    print(cnt)
