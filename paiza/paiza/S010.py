T, B, U, D, L, R = (int(x) for x in input().split())
N = int(input())

List = []
for i in range(N):
    List.append(int(input()))

n = T
c = 0
for l in List:
    if n == l:
        continue
    elif (n == T and l == B) or (n == B and l == T) or(n == U and l == D)or(n == D and l == U) or (n == L and l == R)or (n == R and l == L):
        c += 2
    else:
        c += 1
    # print("l", l, "c", c)
    n = l

print(c)
