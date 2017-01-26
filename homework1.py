class Line(object):

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        d = ((x2 - x1)**2 + (y2 - y1)**2)**.5

        print d

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        m = float((y2-y1))/(x2-x1)
        print m


class Cylinder(object):

    # class object Attributes
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        v = self.pi * self.radius**2 * self.height
        print v

    def surface_area(self):
        # I used lateral surfaceare,  Jose used top surface area
        lsa = 2 * self.pi * self.radius * self.height
        print "Lateral surface area: %s" % lsa

        top = self.pi * self.radius**2
        tsa = 2 * top + lsa
        print "Top surface area:  %s" % tsa


def main():
    print 'Line'
    print ''
    coordinate1 = (3, 2)
    coordinate2 = (8, 10)
    li = Line(coordinate1, coordinate2)

    li.distance()

    li.slope()
    print ''
    print 'Cylinder'
    print ''

    c = Cylinder(2, 3)
    c.volume()
    c.surface_area()

if __name__ == '__main__':
    main()
