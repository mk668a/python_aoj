from itertools import combinations

n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))
res = []

for i in range(1, len(A) + 1):
    res.extend(list(combinations(A, i)))

s = []
for r in res:
    s.append(sum(r))

for m in M:
    if m in s:
        print("yes")
    else:
        print("no")
