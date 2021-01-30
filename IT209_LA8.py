#--------------------------------------------------------------------------
# Class: IT 209-001
 
# Lab Assignment #8: Extending the "List" Built- In Class

# Purpose: To create a Python program t to extend the built-in
#          ‘List’ class by creating a derived class ‘IntegerList’.

# Author: Amanpreet Rathore

# Date: 10/30/2019
#--------------------------------------------------------------------------


class IntegerList(list):

    def validIntList(self):
        for i in self:
            if not isinstance (i, int):
                return False, "Error Input Invalid"
        return True, None
 
    def maxInt(self):
        l1 = self.validIntList()
        if l1[0] == True:
            max1 = self[0]
            for i in self:
                if i > max1:
                    max1=i
            return max1
        else:
            return None
            

    def minInt(self):
        l1 = self.validIntList()
        if l1[0] == True:
            min1 = self[0]
            for i in self:
                if i < min1:
                    min1=i
            return min1
        else:
            return None

    def printIntList(self):
        l1 = self.validIntList()
        if l1[0] == True:
            print("Integer List: ", self)
        else:
            print("Error")
                

IL1 = IntegerList([123,13,24,33])
IL2 = IntegerList([123,13,"QWERTY",33])
print('\nList IL1: ')
IL1.printIntList()
print('Largest integer= ', IL1.maxInt())
print('Smallest integer= ', IL1.minInt())
print('\nList IL2: ')
IL2.printIntList()
print('Largest integer= ', IL2.maxInt())
print('Smallest integer= ', IL2.minInt())

        
                    







