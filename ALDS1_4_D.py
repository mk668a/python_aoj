from collections import deque

n, k = map(int, input().split())
t = []
q = deque()
for i in range(n):
    # t[i] = int(input())
    t.append(int(input()))

t.sort()
l = int(len(t) / 2)
t = t[l:] + t[:l]
print(t)
for i in t:
    q.append(i)

sum = []
for i in range(k):
    if len(q) == 1:
        sum.append(q[0])
    else:
        sum.append(q.pop() + q.popleft())

print(sum)
print(max(sum))
