# coding=utf-8
import random
import math

from matplotlib import pyplot

from geometry import Point


def points_in_circle(num=100, circle_r=10, circle_x=0, circle_y=0):
    def gen():
        # random angle
        alpha = 2 * math.pi * random.random()
        # random radius
        r = circle_r * random.random()
        # calculating coordinates
        x = r * math.cos(alpha) + circle_x
        y = r * math.sin(alpha) + circle_y

        return Point(x, y)

    return [gen() for i in xrange(num)]


def points_on_circle(num=100, circle_r=10, circle_x=0, circle_y=0):
    def gen():
        # random angle
        alpha = 2 * math.pi * random.random()
        # random radius
        r = circle_r
        # calculating coordinates
        x = r * math.cos(alpha) + circle_x
        y = r * math.sin(alpha) + circle_y

        return Point(x, y)

    return [gen() for i in xrange(num)]


def points_on_vector(num, xx1, yy1, xx2, yy2, range=1000):
    def gen():
        sign_x = -1 if random.random() < 0.5 else 1

        x1 = float(xx1)
        y1 = float(yy1)
        x2 = float(xx2)
        y2 = float(yy2)

        x = None
        y = range + 1.0
        while abs(y) > range:
            x = random.random() * range * sign_x
            y = (y2 - y1) * (x - x1) / (x2 - x1) + y1

        return Point(x, y)

    return [gen() for i in xrange(num)]


def points_on_segment(num, xx1, yy1, xx2, yy2):
    if yy2 < yy1:
        temp = yy1
        yy1 = yy2
        yy2 = temp
        temp = xx1
        xx1 = xx2
        xx2 = temp

    def gen():
        x1 = float(xx1)
        y1 = float(yy1)
        x2 = float(xx2)
        y2 = float(yy2)

        x = x2 + 1.0
        y = y2 + 1.0
        if x1 != x2:
            while y > y2:
                x = random.random() * (x2 - x1) + x1
                y = (y2 - y1) * (x - x1) / (x2 - x1) + y1
        else:
            while x > x2:
                y = random.random() * (y2 - y1) + y1
                x = (x2 - x1) * (y - y1) / (y2 - y1) + x1

        return Point(x, y)

    return [gen() for i in xrange(num)]


def points_by_coors(num=100, max_x=100, max_y=100):
    def gen():
        sign_x = -1 if random.random() < 0.5 else 1
        sign_y = -1 if random.random() < 0.5 else 1

        x = random.random() * max_x * sign_x
        y = random.random() * max_y * sign_y

        return Point(x, y)

    return [gen() for i in xrange(num)]


def points_on_rectangle(num=100, x1=-10, x2=10, y1=-10, y2=10):
    return points_on_segment(num / 4, x1, y1, x2, y1) + \
           points_on_segment(num / 4, x1, y1, x1, y2) + \
           points_on_segment(num / 4, x2, y2, x2, y1) + \
           points_on_segment(num / 4, x1, y2, x2, y2)


def points_weird(num1=25, num2=20, x=10, y=10):
    return points_on_segment(num1, 0, 0, x, 0) + \
           points_on_segment(num1, 0, 0, 0, y) + \
           points_on_segment(num2, 0, 0, x, y) + \
           points_on_segment(num2, 0, y, x, 0) + \
            [(0, 0), (x, y), (0, y), (x, 0)]


def format_points(points):
    out = ''
    for x, y in points:
        out += '{:10.4f}, {:10.4f}\n'.format(x, y)
    return out


def format_c(points):
    out = ''
    for x, y in points:
        out += '{:10.4f} {:10.4f}\n'.format(x, y)
    return out


def first_task():

    points_a = points_by_coors(15, max_x=1000000, max_y=1000000)
    pyplot.plot([a.x for a in points_a], [a.y for a in points_a], 'bo')
    pyplot.title('Losowe na wspolrzednych')
    pyplot.savefig('points_by_coors.png')
    pyplot.close()

    points_b = points_on_circle()
    pyplot.plot([a.x for a in points_b], [a.y for a in points_b], 'bo')
    pyplot.title('Losowe na okregu')
    pyplot.savefig('points_in_circle.png')
    pyplot.close()

    points_c = points_on_rectangle()
    pyplot.plot([a.x for a in points_c], [a.y for a in points_c], 'bo')
    pyplot.title('Losowe na prostokacie')
    pyplot.savefig('points_on_rectangle.png')
    pyplot.close()

    points_d = points_weird()
    pyplot.plot([a.x for a in points_d], [a.y for a in points_d], 'bo')
    pyplot.title('Losowe na zgodnie z 1.d)')
    pyplot.savefig('points_weird.png')
    pyplot.close()

    return points_a, points_b, points_c, points_d
