N, M, Q = (int(x)for x in input().split())
ABF, op_q, group = [], [], []

for i in range(M):
    ABF.append(list(map(int, input().split())))

for i in range(Q):
    li = list(input().split())
    op_q.append([li[0], int(li[1])])

for _ in op_q:
    op, q, maxv = _[0], _[1], 0

    if op == "+":
        group.append(q)
    else:
        group.remove(q)

    if len(group) == 0:
        print("0")
    else:
        for g in group:
            for abf in ABF:
                a, b, f = abf[0], abf[1], abf[2]
                if ((b not in group and g == a) or (a not in group and g == b)) and maxv < f:
                    maxv = f
        print(maxv)
