n = int(input())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b[2:])

t = []
for i in range(n):
    t.append([0, 0, 0])
time = 0


def dfs(u):
    global time
    t[u][2] = 1
    time += 1
    t[u][0] = time
    for v in a[u]:
        if not t[v - 1][2]:
            dfs(v - 1)
    time += 1
    t[u][1] = time


for i in range(n):
    if not t[i][2]:
        dfs(i)

for x in range(n):
    print(x + 1, t[x][0], t[x][1])
