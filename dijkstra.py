def Dijkstra(u, w):
    Q = [i for i in range(n)]
    if len(Q) != 0:
        Q.remove(u)
        for next in G[u]:
            v = next[0]
            u_to_v = next[1]
            if distance[v] > u_to_v + w:
                distance[v] = u_to_v + w
            Dijkstra(v, u_to_v + w)


n = 8
G = [[[1, 5], [4, 9], [7, 8]], [[3, 15], [2, 12], [7, 4]], [[3, 3], [6, 11]], [
    [6, 9]], [[5, 4], [7, 5], [6, 20]], [[2, 1], [6, 13]], [], [[2, 7], [5, 6]]]

# 入力する場合
n = int(input())
G = []
for i in range(n):
    G.append([])
    b = list(map(int, input().split()))
    for j in range(0, len(b) - 1, 2):
        G[i].append([b[j], b[j + 1]])

inf = 9999
distance = [inf] * n
start = 0
distance[start] = 0
Dijkstra(start, 0)
for i in distance:
    print(i)
