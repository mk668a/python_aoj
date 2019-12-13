def partition(a, p, r):
    x = a[r]
    i = p-1
    for j in range(p, r):
        if a[j] <= x:
            i = i+1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1


n = int(input())
a = list(map(int, input().split()))
res = partition(a, 0, n-1)
for k in range(n):
    if(k == res):
        print("["+str(a[k])+"] ", end="")
    elif(k == n-1):
        print(str(a[k]))
    else:
        print(str(a[k])+" ", end="")
