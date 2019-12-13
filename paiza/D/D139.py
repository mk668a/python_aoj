n = int(input())
S = input().split()

g, p = 0, 0
for s in S:
    if s == 'G':
        g += 1
    else:
        p += 1

if g < p:
    print('G')
elif g > p:
    print('P')
else:
    print('Draw')
