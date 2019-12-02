from itertools import combinations

data = ['a', 'b', 'c', 'd', 'e']
result = []

for i in range(1, len(data) + 1):
    result.extend(list(combinations(data, i)))

print(result)
print("要素数: " + str(len(result)))
