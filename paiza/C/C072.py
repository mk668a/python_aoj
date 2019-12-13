ATK, DEF, AGI = (int(x)for x in input().split())
N = int(input())
List = []
for i in range(N):
    List.append(input().split())

flag = 0
for l in List:
    name = l[0]
    MINATK, MAXATK, MINDEF, MAXDEF, MINAGI, MAXAGI = int(
        l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5]), int(l[6])
    if MINATK <= ATK and ATK <= MAXATK and MINDEF <= DEF and DEF <= MAXDEF and MINAGI <= AGI and AGI <= MAXAGI:
        flag = 1
        print(name)

if flag == 0:
    print('no evolution')
