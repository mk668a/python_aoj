S = input()
T = input()
list = []
for i in range(len(S)):
    list.append(S[0:i] + S[i + 1:])
c = 0
for l in list:
    if T == l:
        c += 1
print(c)
