n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
s = []


def solve(i, m):
    global A
    global s

    if m == 0:
        return 1
    if i >= n:
        return 0
    s.append(m)
    s.append(m - A[i])
    res = solve(i + 1, m) or solve(i + 1, m - A[i])
    return res


solve(0, 0)
print(s)
for i in m:
    if i in s:
        print('yes')
    else:
        print('no')
