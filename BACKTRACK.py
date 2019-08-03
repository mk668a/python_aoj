import copy


def BACKTRACK(S):
    global solution
    # S: 可能な選択を保持したリスト
    S1 = copy.copy(S)
    S[0] = S1
    k = 0
    while(k >= 0):
        a = []
        while len(S[k]) != 0:  # 　進める
            print("S[", k, "]:", S[k])
            a.append(S[k].pop(0))
            print("a:", a)
            if a == solution:
                print("solution: ", a)
            k = k + 1
            print("len(S[k - 1])", len(S[k - 1]))
            if len(S[k - 1]) != 0:
                S[k] = S1
            else:
                break
        k = k - 1  # バックトラック


S = [[i for i in range(1, 5)], [i for i in range(3, 6)]]
solution = [1, 2, 3]
BACKTRACK(S)
