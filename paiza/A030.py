N = int(input())
List = list(map(int, input().split()))
nodes = [[] for i in range(N)]

for i in range(N - 1):
    l = List[i]
    nodes[l-1].append(1+i)


def count(n):
    global c
    if len(nodes[n]) == 0:
        return c
    else:
        c += len(nodes[n])
        for i in nodes[n]:
            count(i)


for i in range(N):
    c = 0
    count(i)
    print(c)
