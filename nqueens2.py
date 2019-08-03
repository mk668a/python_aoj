def n_queen(n):
    count = 0
    for board in put_queens(board=[n] * n):
        for queen in board:
            print(''.join('.Q'[x == queen] for x in range(n)))
        print()
        count += 1
    print(count, 'ways')


def put_queens(board, y=0):
    # print("------ y =", y, "------")
    n = len(board)
    if y == n:
        yield board
    else:
        for x in range(n):
            if not conflict(board, x, y):
                board[y] = x
                # print("true,", board)
                yield from put_queens(board, y + 1)


def conflict(board, x, y):
    # print("x =", x)
    # for ty, tx in enumerate(board[:y]):
    #     if tx == x or tx + (y - ty) == x or tx - (y - ty) == x:
    #         return True
    return any(tx == x or tx + (y - ty) == x or tx - (y - ty) == x
               for ty, tx in enumerate(board[:y]))


if __name__ == '__main__':
    n_queen(int(input('n = ')))
