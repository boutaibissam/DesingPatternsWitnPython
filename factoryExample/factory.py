"""
    Author : Issam Boutaib
    date :  18/10/2017
    an example of Factory Design pattern implementation
"""

class Person:

    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getgender(self):
        return self.gender

class Male(Person):

    def __init__(self, name):
        Person.__init__(self)
        self.name = name

    def __str__(self):
        return "Mr. "+ self.name

class Female(Person):

    def __init__(self, name):
        Person.__init__(self)
        self.name = name

    def __str__(self):
        return "Mrs. "+ self.name

#################################################################
#########               FActory                         #########
#################################################################


class Factory:

    def getPerson(self,name, gender):
        if gender == "M":
            return Male(name)
        if gender == "F":
            return Female(name)


#################################################################
#########               Main                            #########
#################################################################

if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson("Chetan", "M")
    print person