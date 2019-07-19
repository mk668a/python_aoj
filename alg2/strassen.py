import random
import time


def DivideMatrix(m, n, n_2, cond):
    k = 0
    a = []
    s, t, u, v = 0, 0, 0, 0
    if cond == "00":
        t = n_2
        v = n_2
    elif cond == "01":
        t = n_2
        u = n_2
        v = n
    elif cond == "10":
        s = n_2
        t = n
        v = n_2
    else:
        s = n_2
        t = n
        u = n_2
        v = n
    for i in range(s, t):
        a.append([])
        for j in range(u, v):
            a[k].append(m[i][j])
        k += 1
    return a


def MAT_MULT(A, B):
    n = len(A)
    C = [["" for i in range(n)] for i in range(n)]
    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        # C[0][0] = MAT_MULT(A[0][0], B[0][0], int(n / 2)) + MAT_MULT(A[0][1], B[1][0], int(n / 2))
        # C[0][1] = MAT_MULT(A[0][0], B[0][1], int(n / 2)) + MAT_MULT(A[0][1], B[1][1], int(n / 2))
        # C[1][0] = MAT_MULT(A[1][0], B[0][0], int(n / 2)) + MAT_MULT(A[1][1], B[1][0], int(n / 2))
        # C[1][1] = MAT_MULT(A[1][0], B[0][1], int(n / 2)) + MAT_MULT(A[1][1], B[1][1], int(n / 2))

        n_2 = int(n / 2)
        A_00 = DivideMatrix(A, n, n_2, "00")
        A_01 = DivideMatrix(A, n, n_2, "01")
        A_10 = DivideMatrix(A, n, n_2, "10")
        A_11 = DivideMatrix(A, n, n_2, "11")

        B_00 = DivideMatrix(B, n, n_2, "00")
        B_01 = DivideMatrix(B, n, n_2, "01")
        B_10 = DivideMatrix(B, n, n_2, "10")
        B_11 = DivideMatrix(B, n, n_2, "11")

        # if n == 2:
        #     C[0][0] = MAT_MULT(A_00, B_00)[0] + MAT_MULT(A_01, B_10)[0]
        #     C[0][1] = MAT_MULT(A_00, B_01)[0] + MAT_MULT(A_01, B_11)[0]
        #     C[1][0] = MAT_MULT(A_10, B_00)[0] + MAT_MULT(A_11, B_10)[0]
        #     C[1][1] = MAT_MULT(A_10, B_01)[0] + MAT_MULT(A_11, B_11)[0]
        # else:
        c_00, c_01, c_10, c_11 = [], [], [], []
        for i in range(n_2):
            mat = MAT_MULT(A_00, B_00)[0][i] + MAT_MULT(A_01, B_10)[0][i]
            # print(mat)
            c_00.append(mat)
        for i in range(n_2):
            mat = MAT_MULT(A_00, B_01)[0][i] + MAT_MULT(A_01, B_11)[0][i]
            # print(mat)
            c_01.append(mat)
        for i in range(n_2):
            mat = MAT_MULT(A_10, B_00)[0][i] + MAT_MULT(A_11, B_10)[0][i]
            # print(mat)
            c_10.append(mat)
        for i in range(n_2):
            mat = MAT_MULT(A_10, B_01)[0][i] + MAT_MULT(A_11, B_11)[0][i]
            # print(mat)
            c_11.append(mat)
        C[0][0] = c_00
        C[0][1] = c_01
        C[1][0] = c_10
        C[1][1] = c_11
        # C[0][0] = MAT_MULT([[A[0][0]]], [[B[0][0]]], int(n / 2))[0][0] + MAT_MULT([[A[0][1]]], [[B[1][0]]], int(n / 2))[0][0]
        # C[0][1] = MAT_MULT([[A[0][0]]], [[B[0][1]]], int(n / 2))[0][0] + MAT_MULT([[A[0][1]]], [[B[1][1]]], int(n / 2))[0][0]
        # C[1][0] = MAT_MULT([[A[1][0]]], [[B[0][0]]], int(n / 2))[0][0] + MAT_MULT([[A[1][1]]], [[B[1][0]]], int(n / 2))[0][0]
        # C[1][1] = MAT_MULT([[A[1][0]]], [[B[0][1]]], int(n / 2))[0][0] + MAT_MULT([[A[1][1]]], [[B[1][1]]], int(n / 2))[0][0]
    # print(C)
    print()
    return C


def Strassens(A, B):
    n = len(A)
    C = [["" for i in range(n)] for i in range(n)]
    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        n_2 = int(n / 2)
        A_00 = DivideMatrix(A, n, n_2, "00")
        A_01 = DivideMatrix(A, n, n_2, "01")
        A_10 = DivideMatrix(A, n, n_2, "10")
        A_11 = DivideMatrix(A, n, n_2, "11")

        B_00 = DivideMatrix(B, n, n_2, "00")
        B_01 = DivideMatrix(B, n, n_2, "01")
        B_10 = DivideMatrix(B, n, n_2, "10")
        B_11 = DivideMatrix(B, n, n_2, "11")

        if n = 2:
            S1 = B_01 - B_11
            S2 = A_00 + A_01
            S3 = A_10 + A_11
            S4 = B_10 - B_00
            S5 = A_00 + A_11
            S6 = B_00 + B_11
            S7 = A_01 - A_11
            S8 = B_10 + B_11
            S9 = A_00 - A_10
            S10 = B_00 + B_01
        else:
            # S1 = B_01 - B_11
            # S2 = A_00 + A_01
            # S3 = A_10 + A_11
            # S4 = B_10 - B_00
            # S5 = A_00 + A_11
            # S6 = B_00 + B_11
            # S7 = A_01 - A_11
            # S8 = B_10 + B_11
            # S9 = A_00 - A_10
            # S10 = B_00 + B_01

        P1 = Strassens(A_00, S1)
        P2 = Strassens(S2, B_11)
        P3 = Strassens(S3, B_00)
        P4 = Strassens(A_11, S4)
        P5 = Strassens(S5, S6)
        P6 = Strassens(S7, S8)
        P7 = Strassens(S9, S10)

        # C = [["" for i in range(2)] for i in range(2)]
        C[0][0] = P5 + P4 - P2 + P6
        C[0][1] = P1 + P2
        C[1][0] = P3 + P4
        C[1][1] = P1 + P5 - P3 - P7
    return C


def CreateMatrix(m, n):
    mat = []
    for i in range(m):
        mat.append([])
        for j in range(n):
            ran = random.randint(1, 9)
            mat[i].append(ran)
    return mat


# matrix = [32, 64, 128, 256, 512, 1024]
matrix = [4]
for n in matrix:
    print("matrix: ", n, " * ", n)
    # A = CreateMatrix(n, n)
    # B = CreateMatrix(n, n)
    # A = [[1, 3], [7, 5]]
    # B = [[6, 8], [4, 2]]
    A = [[2, 3, 4, 6], [1, 4, 2, 7], [2, 1, 3, 6], [3, 4, 5, 6]]
    B = [[3, 1, 2, 1], [2, 4, 2, 4], [4, 3, 5, 3], [6, 3, 5, 5]]

    print(A)
    print(B)

    Recursive_s = time.time()
    C = MAT_MULT(A, B)
    Recursive_e = time.time()
    for c in C:
        print(c)
    print("Recursive:", round(Recursive_e - Recursive_s, 8))

    Strassen_s = time.time()
    C = Strassens(A, B)
    Strassen_e = time.time()
    for c in C:
        print(c)
    print("Strassen:", round(Strassen_e - Strassen_s, 8))

    print()
