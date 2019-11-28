H, W, N = (int(x)for x in input().split())
l = []
for i in range(N):
    l.append(list(map(int, input().split())))
# print(l)

r = [['.' for i in range(W)] for j in range(H)]

for i in range(len(l)):
    h_i = l[i][0]
    w_i = l[i][1]
    x_i = l[i][2]

    add_h = 0
    flag = 0
    for j in reversed(range(H)):
        for k in range(x_i, x_i+w_i):
            if(r[j][k] == "#"):
                add_h = j+1
                flag = 1
                break
        if(flag == 1):
            break

    for j in range(0, h_i):
        for k in range(x_i, x_i+w_i):
            # print("j k", j+l[i-1][0], k)
            new_h = j + add_h
            r[new_h][k] = "#"

for h in reversed(r):
    for w in h:
        print(w, end="")
    print()