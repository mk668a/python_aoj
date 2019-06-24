c = list(input().split())

for i in range(int(input())):
    q = list(input().split())
    # print()
    d = c
    for j in range(4):
        d = d[4:5]+d[0:1]+d[2:4]+d[5:6]+d[1:2]
        # d = d[3:4]+d[1:2]+d[0:1]+d[5:6]+d[4:5]+d[2:3]
        for k in range(4):
            d = d[0:1]+d[2:3]+d[4:5]+d[1:2]+d[3:4]+d[5:6]
            # print(d)
            if d[0] == q[0] and d[1] == q[1]:
                print(d[2])
                break
        if d[0] == q[0] and d[1] == q[1]:break
    if (d[0] == q[0] and d[1] == q[1]) == False:
        d = d
        for j in range(4):
            d = d[3:4]+d[1:2]+d[0:1]+d[5:6]+d[4:5]+d[2:3]
            # d = d[4:5]+d[0:1]+d[2:4]+d[5:6]+d[1:2]
            for k in range(4):
                d = d[0:1]+d[2:3]+d[4:5]+d[1:2]+d[3:4]+d[5:6]
                # print(d)
                if d[0] == q[0] and d[1] == q[1]:
                    print(d[2])
                    break
            d = d
            if d[0] == q[0] and d[1] == q[1]:break
