def run(self):
    hull = copy(self.hull)
    p0 = hull[0]
    p1 = hull[1]
    other_points = hull[2:-1]

    while True:
        other_points = sorted(
        	other_points, 
        	key=lambda point: cosinus(p0, point, p1), 
        	reverse=True
        )

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
            x = complex(p0.x, p0.y) 
            y = complex(p1.x, p1.y)
            z = complex(v.x, v.y)
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

