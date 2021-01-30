#--------------------------------------------------------------------------
# Class: IT 209-001
 
# Assignment #10: Property Decorator

# Purpose: To create a program to u enhance the Python program
#           created in Lab #3 to define a class to model the
#           characteristics of a general employee.

# Author: Amanpreet Rathore

# Date: 11/13/2019
#--------------------------------------------------------------------------

class Employee():
    """ Employee Class - used to create Employee objects 
        ------------------------------------------------ """ 
    def __init__(self, empl_num, name, birth_year, birth_month, job_title, salary):
        self.__empl_num = str(empl_num) 
        self.__name = str(name)
        self.__birth_year = birth_year
        self.__birth_month = birth_month
        self.__job_title = str(job_title)
        self.__salary = salary

    def __str__ (self):
        return (self.__name + ', '+self.__job_title +', ' + str(self.__salary))

    @property
    def name (self):
        return self.__name

    @name.setter
    def _set_name (self, name):
        if not name : # name cannot be blank or None
            raise Exception ("Invalid Name")
        self.__name = name
    
    @property
    def job_title (self):
        return self.__job_title        

    @job_title.setter
    def setJob_title(self, job_title):
        if not job-title : # name cannot be blank or None
            raise Exception ("Invalid Job Title")
        self.__job_title = job_title
        return str(job_title)

    def getSalary (self):
        return self.__salary

    def setSalary(self, salary):
        self.__salary = salary
        return int(salary)

    def age (self, this_month, this_year):
        if self.__birth_month < this_month:
            return this_year - self.__birth_year
        else:
            return this_year - self.__birth_year - 1

    salary= property (getSalary, setSalary)

       
print('\nStart of Employee class demo')

e1 = Employee('E34568', 'David Miller', 1960, 3, 'Accountant', 65000)
e2 = Employee('E22154', 'Margarete Smith', 1972, 10, 'Vice President', 115000)
e3 = Employee('E43344', 'Chase Smedley', 1982, 8, 'Salesman', 75000)
e4 = Employee('E12157', 'Daniel Arledge', 1959, 11, 'Lawyer', 92000)
e5 = Employee('E00001', 'Abe Lincoln', 1940, 2, 'Former POTUS', 10000)

print('e1 = ', e1)
print('e2 = ', e2)
print('e3 = ', e3)
print('e4 = ', e4)
print('e5 = ', e5)

print('\nEnd of Employee class demo')

    
