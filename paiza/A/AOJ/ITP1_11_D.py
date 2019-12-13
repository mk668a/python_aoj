a = []
for i in range(int(input())):
    a.append(int(input()))

c = a[1]-a[0]
maxv = c
minv = min(a[0],a[1])
for i in range(2,len(a)):
    maxv = max(a[i] - minv, maxv)
    minv = min(a[i], minv)

print("max = "+str(maxv))
# print(maxv)
