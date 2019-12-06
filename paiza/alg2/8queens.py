def queen(n, y):
    global count
    if n == y and check(n):
        flag = 1
        for i in range(len(r)):
            for j in range(len(board)):
                if r[i][0] == j and r[i][1] != board[j]:
                    flag = 0
                    break
        if flag == 1:
            for i in range(len(board)):
                for j in range(8):
                    p = 'Q' if j == board[i] else '.'
                    print(p, end='')
                print()
            count += 1
            print(count)
            print()
    else:
        for x in range(n):
            if x not in board:
                board[y] = x
                queen(n, y + 1)
                board[y] = 8


def conflict(x, y):
    for y1 in range(y):
        x1 = board[y1]
        if x1 - y1 == x - y or x1 + y1 == x + y:
            return 1
    return 0


def check(n):
    for y in range(1, n):
        if conflict(board[y], y):
            return 0
    return 1


if __name__ == '__main__':
    board = [8] * 8
    r = []
    count = 0
    queen(8, 0)
