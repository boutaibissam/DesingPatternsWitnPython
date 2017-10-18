"""
    Author : Issam Boutaib
    date :  18/10/2017
    an example of Factory Design pattern implementation
"""

class Shape:

    def __init__(self):
        self.name = None

    def draw(self):
        pass


class Rectangle(Shape):
    def __init__(self):
        pass

    def draw(self):
        print "Drawing a rectangle !"


class Circle(Shape):

    def __init__(self):
        pass

    def draw(self):
        print "Drawing a Circle !"


class Square(Shape):

    def __init__(self, ):
        pass

    def draw(self):
        print "Drawing a Square !"

#################################################################
#########               FActory                         #########
#################################################################

class Factory:

    def getShape(self, name):
        if name == "Circle":
            return Circle()

        if name == "Square":
            return Square()

        if name == "Rectangle":
            return Rectangle()

if __name__ == '__main__':
    factory = Factory()
    shape = factory.getShape("Circle")
    shape1 = factory.getShape("Rectangle")
    shape2 = factory.getShape("Square")
    print shape
    print shape1
    print shape2