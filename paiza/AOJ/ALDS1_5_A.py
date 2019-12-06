# 時間オーバー
def combine(A):
    global s
    n = len(A)

    for std in range(n):
        for i in range(std, n-1):
            v = A[std] + A[i+1]
            s.append(v)
            B = A[:]
            B.pop(std)
            B.pop(i)
            B.insert(0, v)
            combine(B)


n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))
s = A[:]

combine(A)

s_ = list(set(s))
for m in M:
    if m in s_:
        print("yes")
    else:
        print("no")
