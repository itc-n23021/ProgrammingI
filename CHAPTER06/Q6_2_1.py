clsaa Cylinder:
    pi = 3.14

    def __init__(self, radius=1, height=1):
        self.radius = float(radius)
        self.height = float(height)

    def calc_base_area(self):
        pi = Cylinder.pi
        r = self.radius
        return pi * r * r

    def calc_side_area(self):
        pi = Cylinder.pi
        r = self.radius
        h = self.height
        return 2 * pi * r * h

    def calc_surface_area(self):
        c = self.calc_base_area()
        s = self_calc_side_area()
        return 2 * c + s

    def calc_volume(self):
        c = self.calc_base_area()
        s = self.calc_base_area()
        return c * h

    def show_results(self)
    r = self.radius
    h = self.height
    S = self.calc_surface_area()
    V = self.calc_volume()
    print('半径: {}, 高さ: {}, 表面積: {}, 体積: {}'.
          format(r, h, S, V))