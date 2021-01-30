#--------------------------------------------------------------------------
# Class: IT 209-001
 
# Lab Assignment #6: Polygon Class Inheritance

# Purpose: To create a Python program to define a base class ‘Polygon’.
#          Specifically, the to create three derived subclasses to calculate the
#          area of their respective object class type.

# Author: Amanpreet Rathore

# Date: 10/16/2019
#--------------------------------------------------------------------------

class Polygon:
    sides= []
    def init(self, noOfSides=0 ):
        self.noOfSides = 0
        Polygon.sides.append(self)

    def inputSides(self):
        num=int(input("Enter number of Sides: "))
        Polygon.sides.append(num)
        return sides

    def dispSides(self):
        for i in sides:
            return ("List of sides: ", i )

class Triangle(Polygon):
    
    def __init__(self):
        return(Polygon.init(3))

    def findArea(self):
        #width:
        #a = side 1
        #b = side 2
        #c = side 3
        s = (a+b+c) / 2                      #semi-perimeter
        
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5     #area

        return area

class Square(Polygon):

    def __init__ (self):
            return(Polygon.init(1))

    def findArea(self):
            #width:
            #a = side 1
            area= a ** 2
            return area

class Rectangle(Polygon):

    def __init__(self):
            return(Polygon.init(2))

    def findArea(self):
        #width:
        #a = side 1
        #b = side 2
        area = a*b
        return area

print("For the Triangle class: ")
t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()

print("For the Square class: ")
sq = Square()
sq.inputSides(1)
sq.dispSides()
sq.findArea()

print("For the Rectangle class: ")
r = Rectangle()
r.inputSides(2)
r.dispSides()
r.findArea()

    
