y, m, d = (int(x) for x in input().split())
a, b = (int(x) for x in input().split())

c = 0

if(m % 2 == 0):
    c += 15 - d
else:
    c += 13 - d
m += 1

while y % 4 != 1:
    if(m % 2 == 0):
        c += 15
    else:
        c += 13
    m += 1
    if(m == 14):
        m = 1
        y += 1

for i in range(1, a):
    if(i % 2 == 0):
        c += 15
    else:
        c += 13

if(a % 2 == 0):
    c += b
else:
    c += b

print(c)
