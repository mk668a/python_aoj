c = list(input().split())
d = list(input())

for i in range(len(d)):
    if d[i] == "S":
        c = c[4:5]+c[0:1]+c[2:4]+c[5:6]+c[1:2]
    elif d[i] == "N":
        c = c[1:2]+c[5:6]+c[2:4]+c[0:1]+c[4:5]
    elif d[i] == "W":
        c = c[2:3]+c[1:2]+c[5:6]+c[0:1]+c[4:5]+c[3:4]
    elif d[i] == "E":
        c = c[3:4]+c[1:2]+c[0:1]+c[5:6]+c[4:5]+c[2:3]
        
print(c[0])
