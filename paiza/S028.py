N, S = int(input()), [int(x) for x in list(input())]

if N % 3 == 0:
    a = b = c = N/3
else:
    a, b = int(N/3), int(N/3)
    c = N - a - b

S += S
minv = N
for i in range(N):
    A, B, C = S[i:i+a], S[i+a:i+a+b], S[i+a+b:i+a+b+c]
    l = [sum(A), sum(B), sum(C)]
    v = max(l) - min(l)
    if v < minv:
        minv = v

print(minv)
