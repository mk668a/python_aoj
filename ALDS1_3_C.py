# from collections import deque
#
# l = deque()
# delete = 0
# order = int(input())
# if order > 2 * 10**6:
#     order = 2 * 10**6
#
#
# for i in range(order):
#     a = input().split()
#     if len(l) > 10**6:
#         break
#     if a[0] == 'insert' and len(a) == 2 and 0 <= int(a[1]) and int(a[1]) <= 10**9:
#         l.appendleft(int(a[1]))
#     elif a[0] == 'delete' and len(a) == 2 and 0 <= int(a[1]) and int(a[1]) <= 10**9:
#         delete += 1
#         if int(a[1]) in l and delete < 21:
#             l.remove(int(a[1]))
#     elif a[0] == 'deleteFirst':
#         l.popleft()
#     elif a[0] == 'deleteLast':
#         l.pop()
#
# print(*l)

from collections import deque
l = deque()
for i in range(int(input())):
    a = input()
    if a[6] == 'F':
        l.popleft()
    elif a[6] == 'L':
        l.pop()
    elif a[0] == 'i':
        l.appendleft(a[7:])
    elif a[0] == 'd':
        if a[7:] in l:
            l.remove(a[7:])
print(*l)
