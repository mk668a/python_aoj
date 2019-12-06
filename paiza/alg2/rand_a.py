def RAND1(n):
    x = 53402397
    rand_seq = []
    for i in range(n):
        x = 65539 * x + 125654
        if x < 0:
            x += 2147483647
            x += 1
        rand_seq.append(x)
    return rand_seq


def RAND2(n):
    x = 1
    A = 48271
    M = 2147483647
    Q = M / A
    R = M % A
    rand_seq = []
    for i in range(n):
        x = A * (x % Q) - R * (x / Q)
        if x < 0:
            x += M
        rand_seq.append(x)
    return rand_seq


def RAND3(n):
    x = 1
    next = 0
    A = RAND2(55)
    rand_seq = []
    for i in range(n):
        j = (next + 31) % 55
        x = A[j] - A[next]
        if x < 0:
            x += 2147483647
            x += 1
        A[next] = x
        next = (next + 1) % 55
        rand_seq.append(x)
    return rand_seq


n = 5
print("RAND1(" + str(n) + ")")
print(RAND1(n), end='\n\n')

print("RAND2(" + str(n) + ")")
print(RAND2(n), end='\n\n')

print("RAND3(" + str(n) + ")")
print(RAND3(n), end='\n\n')
