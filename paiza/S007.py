import re

S = input()

# 一番小さいカッコの中身
pattern = '\d+[a-z]'
find = re.findall(pattern, S)

for i in range(len(find)):
    f = re.search(pattern, S)
    if f:
        s = f.start()
        e = f.end()
        d = re.findall('\d+|[a-z]', f.group())
        S = S[:s] + int(d[0]) * d[1] + S[e:]

pattern = '\d+\\([a-z]+\\)'
find = re.findall(pattern, S)
for j in range(len(find)):
    find = re.findall(pattern, S)
    # print(find)
    if len(find) == 0:
        break
    for i in range(len(find)):
        f = re.search(pattern, S)
        if f:
            s = f.start()
            e = f.end()
            d = re.findall('\d+|[a-z]+', f.group())
            S = S[:s] + int(d[0]) * d[1] + S[e:]
            find = re.findall(pattern, S)

for i in range(97, 123):
    print(chr(i), S.count(chr(i)))
