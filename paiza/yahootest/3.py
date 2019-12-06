from itertools import combinations

# 標準入力から2行入力
# 1行目 データ処理工程の個数nを入力
n = int(input())
# 2行目 空白区切りで、データ処理工程にかかる時間を入力
A = list(map(int, input().split()))


sum = []
s = 0
# 1つ目の工程から各工程までのデータ処理工程にかかる時間を配列にする (配列sum)
for i in range(n):
    s += A[i]
    sum.append(s)

# 配列sumの全ての組み合わせを取得する (配列res)
res = []
for i in range(1, len(sum) + 1):
    res.extend(list(combinations(sum, i)))

com = []
for r in res:
    s.append(r)
print(min(com))
