def min(x, y):
    if x <= y:
        return x
    else:
        return y


def max(x, y):
    if x <= y:
        return y
    else:
        return x


n = 8
t = [[-1 for i in range(n)] for j in range(n)]
print(t)
w = [
    [1, 1, 0, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1]
]

for i in range(n):
    for j in range(n):
        if i == j or w[i][j] != 0:
            t[i][j] = 1
        else:
            t[i][j] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            t[i][j] = max(t[i][j], t[i][k] and t[k][j])

for i in range(n):
    print(t[i])
