n = int(input())
A = []

for i in range(n):
    data = list(input().split())
    A.append(data)

currentDate = A[0][0]
maxNumber = 0
food = [0]


# for i in range(n):
#     if A[i][0] == currentDate:
#         foodName = A[i][1]
#         for a in A:
#             if foodName == a[1]:
#                 A[i] = int(A[i])+int(a[3])

for i in range(n):
    if A[i][0] == currentDate:
        foodNum = int(A[i][3])
        if maxNumber < foodNum:
            maxNumber = foodNum
            food[0] = i
        elif maxNumber == foodNum:
            food.append(i)
    else:
        # print(food)
        for f in food:
            print(*A[f])
        currentDate = A[i+1][0]
        maxNumber = 0
