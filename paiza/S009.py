import copy
import itertools

n, S, m, P_n, R = int(input()), list(
    map(int, input().split())), int(input()), [], []

for i in range(m):
    P_n.append(list(map(int, input().split())))


def changeS(S, p):
    S_ = copy.copy(S)
    for i in range(n):
        a = p[i] - 1
        b = S[i]
        S_[a] = b
    return S_


for P in P_n:
    R.append(changeS(S, P))

numP_n = [i for i in range(m)]
newP_n = list(itertools.permutations(numP_n))

for P in newP_n:
    S_ = copy.copy(R[P[0]])
    for i in range(1, len(P)):
        S_ = changeS(S_, P_n[P[i]])
    R.append(S_)

print(*sorted(R)[0])
