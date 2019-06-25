# 入力する場合
# a = [0]
# for i in range(int(input())):
#     a.append(list(map(int, input().split())))

a = [0, [2, 4], [5], [5, 6], [2], [4], []]

t = [0]
for i in range(1, len(a)):
    t.append([False, i])

time = 0


def dfs(u):
    global time
    t[u][0] = True
    time += 1
    t[u].append(time)

    for v in a[u]:
        if not t[v][0]:
            dfs(v)
    time += 1
    t[u].append(time)


for i in range(1, len(a)):
    if not t[i][0]:
        dfs(i)

for x in t[1:]:
    print(*x[2:])
