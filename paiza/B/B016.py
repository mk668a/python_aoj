w, h, n = (int(x) for x in input().split())
x, y = (int(x) for x in input().split())
log = []

for i in range(n):
    l = list(input().split())
    log.append([l[0], int(l[1])])

for l in log:
    d = l[0]
    m = l[1]
    if d == 'U':
        for i in range(m):
            y += 1
            if y >= h:
                y = 0
    if d == 'D':
        for i in range(m):
            y -= 1
            if y < 0:
                y = h-1
    if d == 'R':
        for i in range(m):
            x += 1
            if x >= w:
                x = 0
    if d == 'L':
        for i in range(m):
            x -= 1
            if x < 0:
                x = w-1

print(x, y)
