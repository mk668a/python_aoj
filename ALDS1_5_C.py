import math


def kock(p1, p2, count, left):
    global n
    if count < n:
        count += 1
        # print("count", count)
        # print("left", left)
        # print("p1 =", p1.x, ",", p1.y)
        # print("p2 =", p2.x, ",", p2.y)
        s, t, u = axis(), axis(), axis()

        s.x = (2*p1.x+p2.x)/3
        s.y = (2*p1.y+p2.y)/3
        t.x = (p1.x+2*p2.x)/3
        t.y = (p1.y+2*p2.y)/3
        u.x = ((t.x-s.x)/2) - ((t.y-s.y)*math.sqrt(3)/2) + s.x
        u.y = ((t.x-s.x)*math.sqrt(3)/2) + ((t.y-s.y)/2) + s.y

        kock(p1, s, count, left)
        print("{0:.8f}".format(s.x), "{0:.8f}".format(s.y))
        kock(s, u, count, left+4)
        print("{0:.8f}".format(u.x), "{0:.8f}".format(u.y))
        kock(u, t, count, left+8)
        print("{0:.8f}".format(t.x), "{0:.8f}".format(t.y))
        kock(t, p2, count, left+12)


class axis:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p1 = axis(0, 0)
p2 = axis(100, 0)

n = int(input())
count = 0
print("{0:.8f}".format(p1.x), "{0:.8f}".format(p1.y))
kock(p1, p2, count, 1)
print("{0:.8f}".format(p2.x), "{0:.8f}".format(p2.y))
