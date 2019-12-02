c = 0
n = int(input())
a = list(map(int, input().split()))
f = 1

while f:
    f = 0
    for i in reversed(range(1, n)):
        if a[i - 1] > a[i]:
            c += 1
            b = a[i]
            a[i] = a[i-1]
            a[i-1] = b
            f = 1

print(*a)
print(c)
