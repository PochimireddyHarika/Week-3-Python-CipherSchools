class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def cal_circumference(self):
        return 2*Circle.pi*self.radius

c = Circle(4)
print(c.calc_circumference())
