from matplotlib import pyplot

from geometry import cosinus, plot_points, save_plot, Point
from hull import GrahamHull
from points_generator import points_by_coors

PLOT_AXIS = [-100, 150, -50, 150]


class SmallestRectangle(object):
    hull = None
    points = None
    image_id = 1

    def __init__(self, hull, points):
        self.hull = hull
        self.points = points

    def run(self, mode='area'):
        hull = self.hull + [self.hull[1]]

        min_area = 10 ** 10
        min_perimeter = 10 ** 10
        coords = ()

        for i in xrange(len(hull) - 1):
            center = hull[i]
            t = center.vector(Point(0, 0))
            hull = [p.add_vector(t) for p in hull]

            center = hull[i]
            next_point = hull[i + 1]

            cos = cosinus(next_point, center, Point(1, 0))
            hull = [p.rotate(cos) for p in hull]

            self.plot_stage(hull, mode)

            minx, maxx, maxy = 0, 0, 0
            for p in hull:
                if p.x > maxx:
                    maxx = p.x
                if p.x < minx:
                    minx = p.x
                if p.y > maxy:
                    maxy = p.y

            area = maxy * (maxx - minx)
            perimeter = maxy + maxx - minx
            color = 'ro-'
            if (mode == 'area' and area < min_area) or (mode == 'perimeter' and perimeter < min_perimeter):
                min_area = area
                min_perimeter = perimeter
                coords = minx, maxx, maxy, i
                color = 'go-'

            self.plot_stage_with_rectangle(color, hull, maxx, maxy, minx, mode)

        minx, maxx, maxy, i = coords

        apexes = [
            Point(minx, maxy),
            Point(minx, 0),
            Point(maxx, 0),
            Point(maxx, maxy),
        ]

        hull = self.hull + [self.hull[1]]
        for j in xrange(i + 1):
            center = hull[i]
            t = center.vector(Point(0, 0))
            hull = [p.add_vector(t) for p in hull]
            center = hull[i]
            next_point = hull[i + 1]
            cos = cosinus(next_point, center, Point(1, 0))
            hull = [p.rotate(cos) for p in hull]
            apexes = [p.rotate_cw(cos) for p in apexes]

        apexes = [p.add_vector(Point(0, 0).vector(self.hull[i])) for p in apexes]
        apexes.append(apexes[0])

        fig, ax = pyplot.subplots()
        ax.set_aspect('equal')
        plot_points(apexes, 'go-')
        plot_points(self.points, 'yo')
        plot_points(self.hull, 'b-')
        pyplot.axis(PLOT_AXIS)
        save_plot(mode + '/' + str(self.image_id).zfill(3))
        self.image_id += 1

    def plot_stage_with_rectangle(self, color, hull, maxx, maxy, minx, mode):
        fig, ax = pyplot.subplots()
        ax.set_aspect('equal')
        plot_points(hull, 'bo-')
        plot_points([
            Point(minx, maxy),
            Point(minx, 0),
            Point(maxx, 0),
            Point(maxx, maxy),
            Point(minx, maxy),
        ], color)
        pyplot.axis(PLOT_AXIS)
        save_plot(mode + '/' + str(self.image_id).zfill(3))
        self.image_id += 1

    def plot_stage(self, hull, mode):
        fig, ax = pyplot.subplots()
        ax.set_aspect('equal')
        plot_points(hull, 'bo-')
        pyplot.axis(PLOT_AXIS)
        save_plot(mode + '/' + str(self.image_id).zfill(3))
        self.image_id += 1


if __name__ == "__main__":
    points = points_by_coors(3, 50, 50)

    # Example used on presentation:
    # points = [
    #     Point(0,0),
    #     Point(0,120),
    #     Point(45,-10),
    #     Point(10, 50),
    #     Point(-2, 50),
    #     Point(10, 60),
    #     Point(30, 40),
    #     Point(20, 30),
    #     Point(10, 20),
    #     Point(0, 10),
    #     Point(40, -5),
    # ]

    fig, ax = pyplot.subplots()
    ax.set_aspect('equal')
    plot_points(points, 'bo')
    hull = GrahamHull().run(points)
    plot_points(hull, 'r-')
    pyplot.axis(PLOT_AXIS)
    save_plot('000')
    SmallestRectangle(hull, points).run('area')
    SmallestRectangle(hull, points).run('perimeter')
