a, b, c, d = (str(x)for x in input().split())

li = []
li.append(int(a+b)+int(c+d))
li.append(int(a+b)+int(d+c))

li.append(int(b+a)+int(c+d))
li.append(int(b+a)+int(d+c))

li.append(int(a+c)+int(b+d))
li.append(int(a+c)+int(d+b))

li.append(int(c+a)+int(b+d))
li.append(int(c+a)+int(d+b))

li.append(int(a+d)+int(b+c))
li.append(int(a+d)+int(c+b))

li.append(int(d+a)+int(b+c))
li.append(int(d+a)+int(c+b))

print(max(li))