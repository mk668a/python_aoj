c = 0
for i in range(int(input())):
    a = int(input())
    if pow(2,a-1,a) == 1 or a == 2:
        c += 1
print(c)
