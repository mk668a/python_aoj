H, W = (int(x) for x in input().split())
state = []

for i in range(H):
    state.append([])
    for j in input():
        state[i].append(j)

c = 0
i, j = 0, 0
s = 'r'
while 1:
    if i < 0 or H <= i or j < 0 or W <= j:
        break
    else:
        c += 1
        n = state[i][j]
        if s == 'r':
            if n == '_':
                j += 1
            elif n == '\\':
                i += 1
                s = 'd'
            elif n == '/':
                i -= 1
                s = 'u'
        elif s == 'd':
            if n == '_':
                i += 1
            elif n == '\\':
                j += 1
                s = 'r'
            elif n == '/':
                j -= 1
                s = 'l'
        elif s == 'u':
            if n == '_':
                i -= 1
            elif n == '\\':
                j -= 1
                s = 'l'
            elif n == '/':
                j += 1
                s = 'r'
        elif s == 'l':
            if n == '_':
                j -= 1
            elif n == '\\':
                i -= 1
                s = 'u'
            elif n == '/':
                i += 1
                s = 'd'

print(c)
