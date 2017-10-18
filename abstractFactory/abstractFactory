"""
    Author : Issam Boutaib
    date :  18/10/2017
    an example of Abstract Design pattern implementation
"""

#################################################################
#########               Abstractfactory                 #########
#################################################################

class AbstractFactory:

    def __init__(self):
        pass

    def getShape(self, type):
        pass

    def getColor(self,name):
        pass




#################################################################
#########               shape factory                   #########
#################################################################
class Shape:

    def __int__(self):
        pass


class Square(Shape):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Drawing"+ self.name


class Circle(Shape):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Drawing" + self.name


class Rectangle(Shape):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Drawing"+ self.name


class ShapeFactory(AbstractFactory):

    def __init__(self):
        AbstractFactory.__init__(self)

    def getShape(self, name):
        if name == "Circle":
            return Circle(name)
        if name == "Rectangle":
            return Rectangle(name)
        if name == "Square":
            return Square(name)


#################################################################
#########               Color factory                   #########
#################################################################


class  Color:

    def __int__(self):
        pass


class  Red(Color):

    def __init__(self, name):
        Color.__int__(self)
        self.name = name

    def __str__(self):
        return self.name


class Orange(Color):

    def __init__(self, name):
        Color.__int__(self)
        self.name = name

    def __str__(self):
        return self.name


class Green(Color):
    def __init__(self, name):
        Color.__int__(self)
        self.name = name

    def __str__(self):
        return self.name

class ColorFactory(AbstractFactory):

    def __init__(self):
        AbstractFactory.__init__(self)

    def getColor(self, name):
        if name == "Red":
            return Red(name)
        if name == "Orange":
            return Orange(name)
        if name == "Green":
            return Green(name)






#################################################################
#########               FactoryBuilder                  #########
#################################################################
class FactoryBuilder:

    def __init__(self):
        pass
    def getFactory(self, choice):
        if choice == "shape":
            return ShapeFactory()
        if choice == "color":
            return ColorFactory()


#################################################################
#########               Main                            #########
#################################################################
if __name__ == '__main__':
   factoryBuilser =  FactoryBuilder().getFactory("color").getColor("Green")
   factoryBuilser1 = FactoryBuilder().getFactory("shape").getShape("Rectangle")
   print factoryBuilser
   print factoryBuilser1