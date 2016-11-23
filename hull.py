import math
import sys

eps = 10e-20


class Hull(object):
    root = None
    lowest = None

    @staticmethod
    def det(a, b, c):
        return a.x * b.y + a.y * c.x + b.x * c.y - (b.y * c.x + a.y * b.x + c.y * a.x)

    @staticmethod
    def dist(a, b):
        return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)

    @staticmethod
    def angle_sort(lowest, points):
        if not points:
            return []
        return Hull.angle_sort(
            lowest,
            [x for x in points[1:] if Hull.det(lowest, x, points[0]) > 0]
        ) + [points[0]] + \
       Hull.angle_sort(
           lowest,
           [x for x in points[1:] if not Hull.det(lowest, x, points[0]) > 0]
       )

    def run(self, points):
        raise NotImplementedError

    @staticmethod
    def remove_duplicates(lowest, points):
        if len(points) <= 1:
            return points
        else:
            if abs(Hull.det(lowest, points[0], points[1])) > eps:
                return [points[0]] + Hull.remove_duplicates(lowest, points[1:])
            else:
                point_to_go = points[0] if Hull.dist(lowest, points[0]) > Hull.dist(lowest, points[1]) else points[1]
                return Hull.remove_duplicates(lowest, [point_to_go] + points[2:])


class GrahamHull(Hull):
    def run(self, points):
        sys.setrecursionlimit(100000000)
        points_by_y = sorted(points, key=lambda p: (p.y, p.x))

        self.root = points_by_y[0]

        points = points_by_y[1:]

        points_by_angle = self.angle_sort(self.root, points)
        points_by_angle = self.remove_duplicates(self.root, points_by_angle)
        hull = [self.root, points_by_angle.pop(0), points_by_angle.pop(0)]

        while len(points_by_angle):
            point = points_by_angle.pop(0)
            hull.append(point)
            while len(hull) > 2 and self.det(hull[-3], hull[-2], hull[-1]) < eps:
                hull.remove(hull[-2])

        hull.append(self.root)

        return hull
