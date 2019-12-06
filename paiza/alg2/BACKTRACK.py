import copy


class Node():
    def __init__(self, v):  # コンストラクタ
        self.v = v  # ノードがもつ数値
        self.l = None  # 左エッジ
        self.r = None  # 右エッジ


def BACKTRACK(S):
    global solution
    # S: 可能な選択を保持したリスト
    # S[0] = S1
    A = [S[0]]
    k = 0
    while len(S) > 0:  # 　進める
        # print("S[", k, "]:", S[k])
        node = S.pop(0)
        a_l = node.l
        a_r = node.r
        print("----A----")
        for a in A:
            print("Node:", a.v, "left:", a.l.v, "right:", a.r.v)
        print("--------")
        if A == solution:
            print("----solution----")
            for a in A:
                print("Node:", a.v, "left:", a.l.v, "right:", a.r.v)
            print("--------")
        if a_l != None:
            A.append(a_l)
            print("----left----")
            for a in A:
                print("Node:", a.v, "left:", a.l.v, "right:", a.r.v)
            print("--------")
        if a_r != None:
            A.append(a_r)
            print("----right----")
            for a in A:
                print("Node:", a.v, "left:", a.l.v, "right:", a.r.v)
            print("--------")
        k = k + 1
        # print("len(S[k - 1])", len(S[k - 1]))
        # if len(S[k - 1]) != 0:
        #     S[k] = S1
        # else:
        #     break


def BACKTRACK_R(A, k, S):
    global solution
    # A = a(1), ..., a[k]: 部分解
    if A == solution:
        print("solution: ", end='')
        for a in A:
            print(a.v, end=' ')
        print()
    else:
        node = S[k]
        a_l = node.l
        a_r = node.r
        if a_l != None:
            A_l = copy.copy(A)
            A_l.append(a_l)
            BACKTRACK_R(A_l, a_l.v, S)
        if a_r != None:
            A_r = copy.copy(A)
            A_r.append(a_r)
            BACKTRACK_R(A_r, a_r.v, S)


def CreatTree(n):
    S = [Node(i) for i in range(n)]
    j = 1
    for i in range(0, int((n - 1) / 2)):
        S[i].l = S[j]
        S[i].r = S[j + 1]
        j = j + 2
    # for s in S:
    #     if s.l != None:
    #         print("Node:", s.v, "left:", s.l.v, "right:", s.r.v)
    #     else:
    #         print("Node:", s.v)
    return S


S = CreatTree(15)
solution = [S[0], S[1], S[4], S[10]]
# BACKTRACK(S)
BACKTRACK_R([S[0]], 0, S)
