def ifsame(c, c2):
    d = c
    for j in range(4):
        d = d[4:5]+d[0:1]+d[2:4]+d[5:6]+d[1:2]
        # d = d[3:4]+d[1:2]+d[0:1]+d[5:6]+d[4:5]+d[2:3]
        for k in range(4):
            d = d[0:1]+d[2:3]+d[4:5]+d[1:2]+d[3:4]+d[5:6]
            # print(d)
            if d == c2:
                break
        if d == c2:
            break
    if (d == c2) == False:
        d = d
        for j in range(4):
            d = d[3:4]+d[1:2]+d[0:1]+d[5:6]+d[4:5]+d[2:3]
            # d = d[4:5]+d[0:1]+d[2:4]+d[5:6]+d[1:2]
            for k in range(4):
                d = d[0:1]+d[2:3]+d[4:5]+d[1:2]+d[3:4]+d[5:6]
                # print(d)
                if d == c2:
                    break
            if d == c2:
                break
    if d == c2:
        return True
    else:
        return False


c = []

for i in range(int(input())):
    c.append(list(input().split()))

for i in range(len(c)):
    for j in range(i+1,len(c)):
        if ifsame(c[i],c[j])==True:
            print("No")
            q = 0
            break
        else:
            q = 1
    if q == 0:
        break

if q == 1:
    print("Yes")
