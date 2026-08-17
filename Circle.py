class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius

    def show(self):
        print("Area of Circle = ", self.area())
        print("Perimeter of Circle = ", self.perimeter())

c = Circle(7)
c.show()