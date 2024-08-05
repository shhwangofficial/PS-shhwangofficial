import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
p1 = [x1, y1]
p2 = [x2, y2]
p3 = [x3, y3]
p4 = [x4, y4]


def ccw(p1, p2, p3):
    temp = (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (
        p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1]
    )
    if temp > 0:
        return 1
    elif temp == 0:
        return 0
    else:
        return -1


if ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0 and ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0:
    if (
        ccw(p1, p2, p3) * ccw(p1, p2, p4) == 0
        and ccw(p3, p4, p1) * ccw(p3, p4, p2) == 0
    ):
        if (
            ccw(p1, p2, p3) == 0
            and ccw(p1, p2, p4) == 0
            and ccw(p3, p4, p1) == 0
            and ccw(p3, p4, p2) == 0
        ):
            if y1 == y2:
                if x1 > x2:
                    x1, x2 = x2, x1
                if x3 > x4:
                    x3, x4 = x4, x3
                if x3 <= x2 and x4 >= x1:
                    print(1)
                else:
                    print(0)
            else:
                if y1 > y2:
                    y1, y2 = y2, y1
                if y3 > y4:
                    y3, y4 = y4, y3
                if y3 <= y2 and y4 >= y1:
                    print(1)
                else:
                    print(0)
        else:
            print(1)
    else:
        print(1)
else:
    print(0)
