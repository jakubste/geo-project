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
        if (mode == 'area' and area < min_area) or \
           (mode == 'perimeter' and perimeter < min_perimeter):
            min_area = area
            min_perimeter = perimeter
            coords = minx, maxx, maxy, i
            color = 'go-'

        self.plot_stage_with_rectangle(color, hull, maxx, maxy, minx, mode)

    minx, maxx, maxy, i = coords
