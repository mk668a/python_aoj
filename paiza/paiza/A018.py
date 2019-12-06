import math
W, H, M, N = (int(x)for x in input().split())

C = []
for i in range(M):
    C.append(list(map(int, input().split())))

O = []
for i in range(N):
    O.append(list(map(int, input().split())))


def hit_sector(center_x, center_y, target_x, target_y, start_angle, end_angle, radius):
    dx = target_x - center_x
    dy = target_y - center_y
    sx = math.cos(math.radians(start_angle))
    sy = math.sin(math.radians(start_angle))
    ex = math.cos(math.radians(end_angle))
    ey = math.sin(math.radians(end_angle))

    # 円の内外判定
    if dx ** 2 + dy ** 2 > radius ** 2:
        return False

    # 扇型の角度が180を超えているか
    if sx * ey - ex * sy > 0:
        # 開始角に対して左にあるか
        if sx * dy - dx * sy < 0:
            return False
        # 終了角に対して右にあるか
        if ex * dy - dx * ey > 0:
            return False
        # 扇型の内部にあることがわかった
        return True
    else:
        # 開始角に対して左にあるか
        if sx * dy - dx * sy >= 0:
            return True
        # 終了角に対して右にあるか
        if ex * dy - dx * ey <= 0:
            return True
        # 扇型の外部にあることがわかった
        return False


for o in O:
    x, y = o[0], o[1]
    f = False
    for c in C:
        dx = x - c[0]
        dy = y - c[1]
        t, d, radius = c[2], c[3], c[4]
        start_angle = t - d/2
        end_angle = start_angle + d

        if(hit_sector(c[0], c[1], x, y, start_angle, end_angle, radius)):
            f = True
    if(f):
        print("yes")
    else:
        print('no')
