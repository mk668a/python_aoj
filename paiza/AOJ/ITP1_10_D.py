r = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))

for p in range(1,4):
    print(sum([abs(x[i] - y[i])**p for i in range(r)])**(1/p))

p = float("inf")
print(max([abs(x[i] - y[i]) for i in range(r)]))
