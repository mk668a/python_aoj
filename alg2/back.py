import numpy as np
import random
import time


def DivideMatrix(m, n, n_2):
    a = []
    dim = [[0, int(n_2), 0, int(n_2)], [int(n_2), n, 0, int(n_2)],
           [0, int(n_2), int(n_2), n], [int(n_2), n, int(n_2), n]]
    for k in range(4):
        d = dim[k]
        a.append([])
        l = 0
        for i in range(d[0], d[1]):
            a[k].append([])
            for j in range(d[2], d[3]):
                a[k][l].append(m[i][j])
            l += 1
    return a


def deleteMatrix(a, b):
    c = np.array(a) - np.array(b)
    return c.tolist()
    # print(a)
    # n = len(a)
    # c = []
    # for i in range(n):
    #     c.append([])
    #     for j in range(len(a[i])):
    #         c[i].append(a[i][j] - b[i][j])
    # return c


def sumMatrix(a, b):
    c = np.array(a) + np.array(b)
    return c.tolist()
    # n = len(a)
    # c = []
    # for i in range(n):
    #     c.append([])
    #     for j in range(len(a[i])):
    #         c[i].append(a[i][j] + b[i][j])
    # return c


def MAT_MULT(A_, B_):
    n = len(A_)
    C_ = [[0 for i in range(n)] for j in range(n)]
    if(n == 1):
        C_[0][0] = A_[0][0] * B_[0][0]
        return C_
    else:
        A = DivideMatrix(A_, n, n / 2)
        B = DivideMatrix(B_, n, n / 2)
        C = DivideMatrix(C_, n, n / 2)

        a11 = A[0]
        a12 = A[2]
        a21 = A[1]
        a22 = A[3]

        b11 = B[0]
        b12 = B[2]
        b21 = B[1]
        b22 = B[3]

        C[0] = sumMatrix(MAT_MULT(a11, b11), MAT_MULT(a12, b21))
        C[1] = sumMatrix(MAT_MULT(a11, b12), MAT_MULT(a12, b22))
        C[2] = sumMatrix(MAT_MULT(a21, b11), MAT_MULT(a22, b21))
        C[3] = sumMatrix(MAT_MULT(a21, b12), MAT_MULT(a22, b22))

        return C


def Strassens(A_, B_):
    n = len(A_)
    C_ = [[0 for i in range(n)] for j in range(n)]
    if(n == 1):
        C_[0][0] = A_[0][0] * B_[0][0]
        return C_
    else:
        A = DivideMatrix(A_, n, n / 2)
        B = DivideMatrix(B_, n, n / 2)
        C = DivideMatrix(C_, n, n / 2)

        a11 = A[0]
        a12 = A[2]
        a21 = A[1]
        a22 = A[3]

        b11 = B[0]
        b12 = B[2]
        b21 = B[1]
        b22 = B[3]

        S1 = deleteMatrix(b12, b22)
        S2 = sumMatrix(a11, a12)
        S3 = sumMatrix(a21, a22)
        S4 = deleteMatrix(b21, b11)
        S5 = sumMatrix(a11, a22)
        S6 = sumMatrix(b11, b22)
        S7 = deleteMatrix(a12, a22)
        S8 = sumMatrix(b21, b22)
        S9 = deleteMatrix(a11, a21)
        S10 = sumMatrix(b11, b12)

        P1 = Strassens(a11, S1)
        P2 = Strassens(S2, b22)
        P3 = Strassens(S3, b11)
        P4 = Strassens(a22, S4)
        P5 = Strassens(S5, S6)
        P6 = Strassens(S7, S8)
        P7 = Strassens(S9, S10)

        C[0] = deleteMatrix(sumMatrix(P5, P4), sumMatrix(P2, P6))
        C[1] = sumMatrix(P1, P2)
        C[2] = sumMatrix(P3, P4)
        C[3] = deleteMatrix(sumMatrix(P1, P5), deleteMatrix(P3, P7))

        return C


# m * n の行列をランダム生成
def CreateMatrix(m, n):
    mat = []
    for i in range(m):
        mat.append([])
        for j in range(n):
            ran = random.randint(1, 9)
            mat[i].append(ran)
    return mat


# テスト
# 分割
# A_ = [[2, 3, 4, 6], [1, 4, 2, 7], [2, 1, 3, 6], [3, 4, 5, 6]]
# print(A_)
# A = DivideMatrix(A_, len(A_), len(A_)/2)
# print(A)

# A = [[1, 3], [7, 5]]
# B = [[6, 8], [4, 2]]
# A = [[7, 5]]
# B = [[4, 2]]
A = [[2, 3, 4, 6], [1, 4, 2, 7], [2, 1, 3, 6], [3, 4, 5, 6]]
B = [[3, 1, 2, 1], [2, 4, 2, 4], [4, 3, 5, 3], [6, 3, 5, 5]]
len_A = len(A)
len_B = len(B)
C = MAT_MULT(A, B)
print(C)
C = Strassens(A, B)
print(C)

matrix = [32, 64, 128, 256, 512, 1024]
for n in matrix:
    print("matrix: ", n, " * ", n)
    A = CreateMatrix(n, n)
    B = CreateMatrix(n, n)
    A = np.matrix(A)
    B = np.matrix(B)
    len_A = len(A)
    len_B = len(B)
    C = [[0 for i in range(len(A))]for j in range(len(A))]

    Recursive_s = time.time()
    C = MAT_MULT(A, B)
    Recursive_e = time.time()
    # 計算結果
    # for c in C:
    #     print(c)
    print("Recursive:", round(Recursive_e - Recursive_s, 8))

    Strassen_s = time.time()
    C = Strassens(A, B)
    Strassen_e = time.time()
    # 計算結果
    # for c in C:
    #     print(c)
    print("Strassens:", round(Strassen_e - Strassen_s, 8))
    print()
