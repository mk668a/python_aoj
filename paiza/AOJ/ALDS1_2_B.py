c = 0
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    minj = i
    for j in range(i+1, n):
        if a[minj] > a[j]:
            # print()
            # print(*a)
            # print("a[minj]: "+str(a[minj]))
            # print("a[j]: "+str(a[j]))
            minj = j
    if a[minj] < a[i]:
        b = a[i]
        a[i] = a[minj]
        a[minj] = b
        c += 1

print(*a)
print(c)
