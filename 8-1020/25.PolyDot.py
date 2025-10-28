import math

def on_segment(x1, y1, x2, y2, x, y):
    cross = (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)
    if abs(cross) > 1e-10:
        return False
    if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
        return True
    return False

def info(dots, dot):
    points = list(dots)
    n = len(points)
    if n < 3:
        return 0.0, False, False

    perimeter = 0.0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        perimeter += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    convex = True
    sign = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        x3, y3 = points[(i + 2) % n]
        cross = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
        if abs(cross) < 1e-10:
            continue
        if sign == 0:
            sign = 1 if cross > 0 else -1
        else:
            if (sign == 1 and cross < 0) or (sign == -1 and cross > 0):
                convex = False
                break
    if sign == 0:
        convex = False

    inside = False
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        if on_segment(x1, y1, x2, y2, dot[0], dot[1]):
            inside = True
            break
    if not inside:
        crossings = 0
        for i in range(n):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]
            if (y1 > dot[1]) != (y2 > dot[1]):
                x_intersect = (x2 - x1) * (dot[1] - y1) / (y2 - y1) + x1
                if dot[0] < x_intersect:
                    crossings += 1
        inside = (crossings % 2 == 1)

    return perimeter, convex, inside