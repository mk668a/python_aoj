m, p, q = (int(x) for x in input().split())

res = m - m*p/100
res = res - res*q/100
print(res)
