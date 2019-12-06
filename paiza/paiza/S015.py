k, s, t = (int(x) for x in input().split())


def insert(k, res):
    k -= 1
    if k == 0:
        res = "ABC"
    else:
        # res = "(A " + insert(k) + " B " + insert(k) + " C)"
        res = "A" + insert(k, res) + "B" + insert(k, res) + "C"
    return res


res = ""
res = insert(k, res)
# print(res)
print(res[s-1:t])
