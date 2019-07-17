import random


def Strassens(A, B):
    global Recursive
    global Strassen
    if type(A) == int:
        # 時間計算量
        Recursive += 1
        C = A * B
    else:
        # 時間計算量
        n = len(A[0])
        Recursive += 7 * n / 2 + n * n
        Strassen += n**2.81

        S1 = B[0][1] - B[1][1]
        S2 = A[0][0] + A[0][1]
        S3 = A[1][0] + A[1][1]
        S4 = B[1][0] - B[0][0]
        S5 = A[0][0] + A[1][1]
        S6 = B[0][0] + B[1][1]
        S7 = A[0][1] - A[1][1]
        S8 = B[1][0] + B[1][1]
        S9 = A[0][0] - A[1][0]
        S10 = B[0][0] + B[0][1]

        P1 = Strassens(A[0][0], S1)
        P2 = Strassens(S2, B[1][1])
        P3 = Strassens(S3, B[0][0])
        P4 = Strassens(A[1][1], S4)
        P5 = Strassens(S5, S6)
        P6 = Strassens(S7, S8)
        P7 = Strassens(S9, S10)

        C = [["" for i in range(2)] for i in range(2)]
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


Recursive = 0
Strassen = 0
n = 32
A = CreateMatrix(n, n)
B = CreateMatrix(n, n)
C = Strassens(A, B)
for c in C:
    print(c)
print("Recursive:", round(Recursive))
print("Strassen:", round(Strassen))
