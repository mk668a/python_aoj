import collections


class Thread:
    def __init__(self, name, time):
        self.name = name
        self.time = time


q = collections.deque()

n, m = map(int, input().split())

for i in range(n):
    a, b = input().split()
    q.append(Thread(a, int(b)))

t = 0
while len(q) != 0:
    n = q.popleft()
    if n.time <= m:
        t += n.time
        print(n.name, str(t))
    else:
        t += m
        n.time -= m
        q.append(n)
