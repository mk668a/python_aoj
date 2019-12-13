import itertools
import numpy as np

s, p = (int(x)for x in input().split())

I = [int(i+1) for i in range(p)]

N = p - 1
elm = []
for i, step in enumerate(I):
    temp = [1] * (N - i)
    b = np.empty((len(temp)))
    b[:] = temp
    # b = b.astype(np.int32)
    elm.append(np.arange(0, p+1, step).reshape(-1, *b))
# print(elm)

res = 0
for x in elm:
    res = res + x
I = np.argwhere(res == p)

result = s
for i in I:
    permu = []
    for n in range(len(i)):
        for number in range(i[n]):
            permu.append(n+1)
    permu = set(itertools.permutations(permu))
    for per in permu:
        ex = s
        for x in per:
            ex = ex * (100 + x) / 100
        if ex > result:
            result = ex

print(round(result))
