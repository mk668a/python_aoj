N = int(input())
ID = {}
L = []
numli = {}
for n in range(N):
    d, p, f = (x for x in input().split())
    L.append([d, p, f])
    ID[d] = {'p': p, 'f': f, 'child': []}
    numli[d] = int(f)


for l in L:
    d, p, f = l[0], l[1], [2]
    if p != 'None':
        ID[p]['child'].append(d)


def clac(parent, i):
    child = ID[i]['child']
    if len(child) == 0:
        return
    else:
        for c in child:
            c_p, c_f, c_child = ID[c]['p'], ID[c]['f'], ID[c]['child']
            numli[parent] += int(c_f)
        for c in child:
            clac(parent, c)


for i in ID:
    clac(i, i)

# print(numli)
maxv = 0
res = []
for n in numli:
    if maxv < numli[n]:
        maxv = numli[n]

print(min([int(x) for x in numli if numli[x] == maxv]))
