def insertionSort(A, N):
    # for i in range(len(A)-1):
    #     print(str(A[i])+" ",end="")
    # print(A[len(A)-1])
    print(*A)
    for i in range(1,N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = v
        # for i in range(len(A)-1):
        #     print(str(A[i])+" ",end="")
        # print(A[len(A)-1])
        print(*A)

N = int(input())
A = list(map(int, input().split()))
insertionSort(A, N)
