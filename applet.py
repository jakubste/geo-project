from copy import copy

from matplotlib import pyplot

from geometry import cosinus, plot_points, save_plot
from hull import GrahamHull
from points_generator import points_on_circle


class Applet(object):
    hull = None
    points = None
    image_id = 1

    def __init__(self, hull, points):
        self.hull = hull
        self.points = points

    def run(self):
        hull = copy(self.hull)
        p0 = hull[0]
        p1 = hull[1]
        other_points = hull[2:-1]

        while True:
            other_points = sorted(other_points, key=lambda point: cosinus(p0, point, p1), reverse=True)

            v = other_points[0]
            cos = cosinus(p0, v, p1)

            self.plot_stage(hull, p0, p1, v)

            if cos < 0:
                v = p0.vector(p1)
                s = p0.add_vector(v.divide(2))

                xy = (s.x, s.y)
                radius = v.divide(2).length
                self.plot_circle(hull, radius, xy)
                break

            if cosinus(p0, p1, v) > 0 and cosinus(v, p0, p1) > 0:
                x, y, z = complex(p0.x, p0.y), complex(p1.x, p1.y), complex(v.x, v.y),
                w = z - x
                w /= y - x
                c = (x - y) * (w - abs(w) ** 2) / 2j / w.imag - x

                xy = (-c.real, -c.imag)
                radius = abs(c + x)
                self.plot_circle(hull, radius, xy)
                break

            if cosinus(p0, p1, v) < 0:
                other_points.remove(v)
                other_points.append(p1)
                p1 = v
            if cosinus(v, p0, p1) < 0:
                other_points.remove(v)
                other_points.append(p0)
                p0 = v

    def plot_stage(self, hull, p0, p1, v):
        fig, ax = pyplot.subplots()
        ax.set_aspect('equal')
        plot_points(hull, 'ro-')
        plot_points([p0, p1], 'g-')
        plot_points([p0, v], 'b-')
        plot_points([p1, v], 'b-')
        save_plot('circle/' + str(self.image_id).zfill(3))
        self.image_id += 1

    def plot_circle(self, hull, radius, xy):
        circle = pyplot.Circle(xy, radius, fill=False, color='g', clip_on=False)
        self.make_plot(circle, hull)

    def make_plot(self, circle, hull):
        fig, ax = pyplot.subplots()
        ax.set_aspect('equal')
        ax.add_artist(circle)
        plot_points(self.points)
        plot_points(hull, 'b-')
        save_plot('circle/' + str(self.image_id).zfill(3))
        self.image_id += 1

if __name__ == "__main__":
    points = points_on_circle(15, 100)
    fig, ax = pyplot.subplots()
    ax.set_aspect('equal')
    plot_points(points, 'bo')
    hull = GrahamHull().run(points)
    plot_points(hull, 'r-')
    save_plot('circle/' + str(0))
    Applet(hull, points).run()
