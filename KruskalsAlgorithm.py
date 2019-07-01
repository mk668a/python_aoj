import array
from collections import namedtuple


Edge = namedtuple("Edge", "start end weight")


class findUnion(object):

    def __init__(self, numOfNodes):
        self.par = array.array("l", range(numOfNodes))
        self.rank = array.array("l", (0 for i in range(numOfNodes)))

    def root(self, node):
        if self.par[node] == node:
            return node
        else:
            r = self.root(self.par[node])
            self.par[node] = r
            return r

    def findSet(self, node1, node2):
        return self.root(node1) == self.root(node2)

    def union(self, node1, node2):
        x = self.root(node1)
        y = self.root(node2)
        if x == y:
            pass
        elif self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


def kruskals(N, edges):
    edges.sort(key=lambda edge: edge.weight)
    uf = findUnion(N)
    mst = []
    for e in edges:
        if not uf.findSet(e.start, e.end):
            uf.union(e.start, e.end)
            mst.append(e)
    return mst


# 入力する場合
# N, Q = map(int, input().split())
# edges = [Edge(*map(int, input().split())) for _ in range(Q)]
N, Q = 7, 11
edges = [Edge(start=0, end=1, weight=7), Edge(start=0, end=3, weight=5), Edge(start=1, end=2, weight=8), Edge(start=1, end=3, weight=9), Edge(start=1, end=4, weight=7), Edge(
    start=2, end=4, weight=5), Edge(start=3, end=4, weight=15), Edge(start=3, end=5, weight=6), Edge(start=4, end=5, weight=8), Edge(start=4, end=6, weight=9), Edge(start=5, end=6, weight=11)]
mst = kruskals(N, edges)
for i in range(len(mst)):
    print(*mst[i])
