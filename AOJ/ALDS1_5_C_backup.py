import math


def div(p1, p2, count, left):
    global n, axises
    if count < n:
        count += 1
        print("count", count)
        print("left", left)
        print("p1 =", p1.x, ",", p1.y)
        print("p2 =", p2.x, ",", p2.y)
        s, t, u = axis(), axis(), axis()

        s.x = (2*p1.x+p2.x)/3
        s.y = (2*p1.y+p2.y)/3
        t.x = (p1.x+2*p2.x)/3
        t.y = (p1.y+2*p2.y)/3
        u.x = ((t.x-s.x)/2) - ((t.y-s.y)*math.sqrt(3)/2) + s.x
        u.y = ((t.x-s.x)*math.sqrt(3)/2) - ((t.y-s.y)/2) + s.y

        axises = axises[:left] + [s, u, t] + axises[left:]
        print("s =", s.x, ",", s.y)
        print("u =", u.x, ",", u.y)
        print("t =", t.x, ",", t.y)
        for a in axises:
            print("{0:.8f}".format(a.x), "{0:.8f}".format(a.y))

        div(p1, s, count, left)
        div(s, u, count, left+4)
        div(u, t, count, left+8)
        div(t, p2, count, left+12)


class axis:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p1 = axis(0, 0)
p2 = axis(100, 0)
axises = [p1, p2]

n = int(input())
count = 0
div(p1, p2, count, 1)

print("answer")
for axis in axises:
    print("{0:.8f}".format(axis.x), "{0:.8f}".format(axis.y))
