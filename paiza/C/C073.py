L = int(input())
u, a, b = (int(x) for x in input().split())
v = int(input())

ta = u*L
tb = v*L
for l in range(1, L):
    if l % a == 0:
        ta += b

if ta == tb:
    print("DRAW")
elif ta > tb:
    print("KAME")
else:
    print("USAGI")
