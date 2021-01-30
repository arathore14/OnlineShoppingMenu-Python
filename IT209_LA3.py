#--------------------------------------------------------------------------
# Class: IT 209-001
 
# Lab Assignment #3: Enhanced Employee Class Program

# Purpose: To create a Enhanced Program to define class to model employee attributes

# Author: Amanpreet Rathore

# Date: 09/18/2019
#--------------------------------------------------------------------------

class Employee():
    """Employee Class- Creates objects based on employees' characteristics
    ----------------------------------------------------------------------"""
    def __init__ (self, empl_num, name, birth_year, birth_month, job_title, salary):
        """Purpose of this __init Function is to intialize all the attributes of this class.
        Setting and Assigning variables to create attributes. """
        self.__empl_num = str(empl_num) # ID: "E" + 5 digits
        self.__name = str(name) # last, first
        self.__birth_month = int(birth_month)# 1-12
        self.__birth_year = int(birth_year) #1800 > ...
        self.__job_title = str(job_title) #{'y','n'}
        self.__salary = int(salary) #0-1000000
    
    def __str__ (self):
        """Purpose of this Function is to structure the attributes in a proper output statement.
        Simple concatenation and casting is used to structure this. """
        return("Employee number = " + str(self.__empl_num)+ ","
        +"Employee name = " + str(self.__name) + ",  " + "Birth name = " + str(self.__birth_month)
        + " , " + "Birth year = " + str(self.__birth_year) + ", " + "Job Title= " + str(self.__job_title) + " , "
        + "Salary= " + str(self.__salary))
    

    #accessor(getter)
    def getJob_title(self):
        """This function allows to retrieve and/ or "get" the value
        for the attribute job_title """
        return self.__job_title
    
    #mutator(setter)
    def setJob_title(self, job_title):
        """This function allows to "set" a new value to the for the attribute
        job_title """
        self.__job_title = str(job_title)
        #return True
        return str(job_title)


    
    #accessor(getter)
    def getSalary(self):
        """This function allows to retrieve and/ or "get" the value
        for the attribute salary """
        return self.__salary
    
    #mutator(setter)
    def setSalary(self, salary):
        """This function allows to "set" a new value to the for the attribute
        job_title """
        self.__salary = int(salary)
        return int(salary)


    
    def hourly_rate (self):
        """Purpose of this Function is to calculate the employees' hourly pay by calling self and dividing salary by 2080
        Simple division is used to determine this. """
        #self.hourly_rate = float(hourly_rate)
        #hourly_rate = (salary / 2080)
        #return(float(hourly_rate))
        return float(self.__salary/2080)
    
    def age (self, today_month, today_year):
        """Purpose of this Function is to calculate the current age for the employee depending on the birth dates given.
        The if Statement is used to determine this. """
        #current_year = 2019
        #current_month = 09
        #age = (today_year-self.birth_year)
        age=0
        if self.__birth_month > 9:
            age = 2019 - self.__birth_year - 1
        else:
            age = 2019 - self.__birth_year
        return age
                
        #today_day = (current_month-birth_month) 
        #age= (str(today_day) + "/" + str(today_year)) 

    def can_retire (self, today_month, today_year):
        """Purpose of this Function is to determine of the employee is able to retire, given his/her age
        The if statement is used to determine this."""
        if  self.age(today_month, today_year) > 65:
            return True
        else:
            return False

    def equalEmpl(self, e_obj):
        if self == e_obj:
            return True
        if not isinstance(e_obj, Employee):
            return False
        return ((self.__empl_num) == (e_obj.__empl_num) and
               (self.__name) == (e_obj.__name))
    
today_month = 9
today_year = 2019

print('\nStart of Employee class demo')

print("\n")

e1 = Employee('E34568', 'David Miller', 1960, 3, 'Accountant', 65000)
e2 = Employee('E22154', 'Margarete Smith', 1972, 10, 'Vice President', 115000)
e3 = Employee('E43344', 'Chase Smedley', 1982, 8, 'Salesman', 75000)
e4 = Employee('E12157', 'Daniel Arledge', 1959, 11, 'Lawyer', 92000)


#VALIDATION:
print("#1")
#Retrieve and print each attribute value from at least one object
#to show that the accessor method works.
print("Employee #1 Salary: ", e1.getSalary())

print("\n#2")
#Change each attribute for at least one object to show the mutator method works.
#Print the resulting new attribute value using the accessor method for that attribute
print("New Employee #2 Job Title: ", e2.setJob_title("Teacher"))
e2.getJob_title()

print("New Employee #2 Salary: ", e2.setSalary(200000))
e2.getSalary()

print("\n#3")
#Create an additional employee object that has some of the same information
#as an existing object to show the ‘equals’ method works.  Print the result of the comparison.
print("Same Employees?")
#Same_Employee_Number
e3=e4
#e3._Employee__empl_num = e4._Employee__empl_num
print("Do Employee #3 and #4 have Same Employee Numbers", e3==e4)

print("\n#4")
#Same_Employee_Name
e3._Employee__name = e4._Employee__name
print("Do Employee #3 and #4 have Same Employee Names? ", e3.equalEmpl(e4))
print("\nEmployee #3: ", e3,"\nEmployee #4: ", e3)

print("\n#5")
#Execute the ‘equals’ method with two objects that are not the same to show
#rejection in when the objects do not have the same state.  Print the result of the comparison.

#NOT_SAME_EMPLOYEE_ 
print("Are Employee #1 and Employee #2 equal? ",e1.equalEmpl(e2))


print('\nEnd of Employee class demo')



        
        
        
    
    
        
        

