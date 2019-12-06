while 1:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    avg = sum(a) / n
    cnt = 0
    for i in range(len(a)):
        if a[i] <= avg:
            cnt += 1
    print(cnt)
