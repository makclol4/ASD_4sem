from math import atan2

def convex_hull(points):
    def angle(p1, p2):
        return atan2(p2[1]-p1[1], p2[0]-p1[0])

    p = min(points, key=lambda x: (x[1], x[0]))

    sorted_points = sorted(points, key=lambda x: (angle(p, x), x[0]**2 + x[1]**2))

    stack = [sorted_points[0], sorted_points[1]]

    for point in sorted_points[2:]:
        while len(stack) >= 2 and det(stack[-2], stack[-1], point) <= 0:
            stack.pop()
        stack.append(point)

    return stack


def det(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


"""Ввод точек"""
points = [(12, 24), (8, 86), (4, 78), (53, 4), (354, 587)]
convex_points = convex_hull(points)
print(convex_points)