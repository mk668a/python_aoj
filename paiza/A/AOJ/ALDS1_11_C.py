def bfs(next, cnt):
    t[next] = cnt
    for v in a[next]:
        if t[v - 1] == -1 or t[v - 1] > cnt + 1:
            bfs(v - 1, cnt + 1)


n = int(input())
a, t, f_inf = [], [-1] * n, float('inf')
for i in range(n):
    a.append(list(map(int, input().split()[2:])))
bfs(0, 0)
for i in range(n):
    print(i + 1, t[i])
