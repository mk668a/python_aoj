n = input()
s = set(map(int, input().split()))
q = input()
t = set(map(int, input().split()))
cnt = 0
for i in s:
    if i in t:
        cnt += 1
print(cnt)
