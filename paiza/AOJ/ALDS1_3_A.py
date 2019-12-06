list = list(map(str, input().split()))
stack = []

for i in list:
    if i in ['+', '-', '*']:
        b = int(stack.pop())
        a = int(stack.pop())
        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
        else:
            stack.append(a * b)
    else:
        stack.append(i)

print(*stack)
