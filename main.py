class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

    def perimeter(self):
        print("The perimeter is...")

class Polymorph(Rectangle):
    def perimeter(self):
        print(2 * (self.length + self.width))


poly = Polymorph(5, 10)

poly.area()
poly.perimeter()

