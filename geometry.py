# coding=utf-8
from math import sqrt

from matplotlib import pyplot
from numpy.ma import arccos


class Point(object):
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def vector(self, other):
        """
        :param other: Point
        :return: Vector
        """
        return Vector(other.x - self.x, other.y - self.y)

    def add_vector(self, vector):
        return Point(self.x + vector.x, self.y + vector.y)

    def rotate(self, cos):
        sin = sqrt(1 - cos**2)
        return Point(
            self.x * cos + self.y * sin,
            - self.x * sin + self.y * cos,
        )

    def rotate_cw(self, cos):
        sin = sqrt(1 - cos**2)
        return Point(
            self.x * cos - self.y * sin,
            self.x * sin + self.y * cos,
        )


class Vector(Point):
    def __repr__(self):
        return u'→[{}, {}]'.format(self.x, self.y)

    def dotproduct(self, other):
        """
        :param other: Vector
        :return: double
        """
        return self.x * other.x + self.y * other.y

    @property
    def length(self):
        return sqrt(self.x**2 + self.y**2)

    def divide(self, a):
        return Vector(self.x / a, self.y / a)


class Segment(object):
    start = None
    end = None

    def __init__(self, a, b):
        if a.x > b.x:
            a, b = b, a
        self.start = a
        self.end = b

    def __repr__(self):
        return '[{}, {}]'.format(
            self.start, self.end
        )


def plot_points(points, style='bo'):
    pyplot.plot([a.x for a in points], [a.y for a in points], style)


def save_plot(name):
    if isinstance(name, int):
        name = str(name).zfill(3)
    pyplot.savefig(str(name), dpi=150)
    pyplot.close()


def cosinus(a, c, b):
    """
    :param a: Point
    :param c: Point
    :param b: Point
    :return: double
    """

    u = c.vector(a)
    v = c.vector(b)

    dotproduct = u.dotproduct(v)

    return dotproduct / (u.length * v.length)
