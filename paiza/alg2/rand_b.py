def RAND1(n):
    x = 53402397
    A = 65539
    M = 2147483647
    C = 125654
    rand_seq = []
    for i in range(n):
        x = A * x + C
        if x < 0:
            x += M
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
    M = 2147483647
    rand_seq = []
    for i in range(n):
        j = (next + 31) % 55
        x = A[j] - A[next]
        if x < 0:
            x += M
            x += 1
        A[next] = x
        next = (next + 1) % 55
        rand_seq.append(x)
    return rand_seq


def count_histogram(R):
    M = 2147483647
    per = [0] * 10
    for r in R:
        num = r / M
        if num >= 0 and num < 0.1:
            per[0] += 1
        elif num >= 0.1 and num < 0.2:
            per[1] += 1
        elif num >= 0.2 and num < 0.3:
            per[2] += 1
        elif num >= 0.3 and num < 0.4:
            per[3] += 1
        elif num >= 0.4 and num < 0.5:
            per[4] += 1
        elif num >= 0.5 and num < 0.6:
            per[5] += 1
        elif num >= 0.6 and num < 0.7:
            per[6] += 1
        elif num >= 0.7 and num < 0.8:
            per[7] += 1
        elif num >= 0.8 and num < 0.9:
            per[8] += 1
        elif num >= 0.9 and num < 1.0:
            per[9] += 1
    return per


N = [10, 1000, 1000000]
for n in N:
    print("n =", n)
    print("RAND1")
    PerRand1 = count_histogram(RAND1(n))
    for i in range(len(PerRand1)):
        PerRand1[i] = PerRand1[i] / n * 100
    print(PerRand1)

    print("RAND2")
    PerRand2 = count_histogram(RAND2(n))
    for i in range(len(PerRand2)):
        PerRand2[i] = PerRand2[i] / n * 100
    print(PerRand2)

    print("RAND3")
    PerRand3 = count_histogram(RAND3(n))
    for i in range(len(PerRand3)):
        PerRand3[i] = PerRand3[i] / n * 100
    print(PerRand3, end='\n\n')
