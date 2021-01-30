#--------------------------------------------------------------------------
# Class: IT 209-001
 
# Lab Assignment #2: Employee Class Definition

# Purpose: To create a program to define class to model employee attributes

# Author: Amanpreet Rathore

# Date: 09/11/2019
#--------------------------------------------------------------------------

class Employee():
    """Employee Class- Creates objects based on employees' characteristics
    ----------------------------------------------------------------------"""
    def __init__ (self, empl_num, name, birth_year, birth_month, job_title, salary):
        """Purpose of this __init Function is to intialize all the attributes of this class.
        Setting and Assigning variables to create attributes. """
        self.empl_num = str(empl_num)
        self.name = str(name)
        self.birth_month = int(birth_month)
        self.birth_year = int(birth_year)
        self.job_title = str(job_title)
        self.salary = int(salary)
    
    def __str__ (self):
        """Purpose of this Function is to structure the attributes in a proper output statement.
        Simple concatenation and casting is used to structure this. """
        return("Employee number = " + str(self.empl_num)+ ","
        +"Employee name = " + str((self.name)) + ",  " + "Birth name = " + str(self.birth_month)
        + " , " + "Birth year = " + str(self.birth_year) + ", " + "Job Title= " + str(self.job_title) + " , "
        + "Salary= " + str(self.salary))
    
    def hourly_rate (self):
        """Purpose of this Function is to calculate the employees' hourly pay by calling self and dividing salary by 2080
        Simple division is used to determine this. """
        #self.hourly_rate = float(hourly_rate)
        #hourly_rate = (salary / 2080)
        #return(float(hourly_rate))
        return float(self.salary/2080)
    
    def age (self, today_month, today_year):
        """Purpose of this Function is to calculate the current age for the employee depending on the birth dates given.
        The if Statement is used to determine this. """
        #current_year = 2019
        #current_month = 09
        #age = (today_year-self.birth_year)
        age=0
        if self.birth_month > 9:
            age = 2019 - self.birth_year - 1
        else:
            age = 2019 - self.birth_year
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
    
today_month = 9
today_year = 2019

print('\nStart of Employee class demo')

print("\n")
e1 = Employee('E34568', 'David Miller', 1960, 3, 'Accountant', 65000)
print('e1 = ', (e1.__str__()))
print('Hourly rate for', e1.name, ' = ', e1.hourly_rate())
print('Age of', e1.name, ' = ', e1.age(today_year,today_month))
print('Retirement eligibility for', e1.name, ' = ', e1.can_retire(today_year,today_month))
print("\n")


e2 = Employee('E22154', 'Margarete Smith', 1972, 10, 'Vice President', 115000)
print('e2 = ', (e2.__str__()))
print('Hourly rate for', e2.name, ' = ', e2.hourly_rate())
print('Age of', e2.name, ' = ', e2.age(today_year,today_month))
print('Retirement eligibility for', e2.name, ' = ', e2.can_retire(today_year,today_month))
print("\n")

e3 = Employee('E43344', 'Chase Smedley', 1982, 8, 'Salesman', 75000)
print('e3 = ', (e3.__str__()))
print('Hourly rate for', e3.name, ' = ', e3.hourly_rate())
print('Age of', e3.name, ' = ', e3.age(today_year,today_month))
print('Retirement eligibility for', e3.name, ' = ', e3.can_retire(today_year,today_month))
print("\n")


e4 = Employee('E12157', 'Daniel Arledge', 1959, 11, 'Lawyer', 92000)
print('e4 = ', (e4.__str__()))
print('Hourly rate for', e4.name, ' = ', e4.hourly_rate())
print('Age of', e4.name, ' = ', e4.age(today_year,today_month))
print('Retirement eligibility for', e4.name, ' = ', e4.can_retire(today_year,today_month))
print("\n")

e5 = Employee('E00001', 'Abe Lincoln', 1940, 2, 'Former POTUS', 10000)
print('e5 = ', (e5.__str__()))
print('Hourly rate for', e5.name, ' = ', e5.hourly_rate())
print('Age of', e5.name, ' = ', e5.age(today_year,today_month))
print('Retirement eligibility for', e5.name, ' = ', e5.can_retire(today_year,today_month))
print("\n")


print('\nEnd of Employee class demo')
        
        
        
        
        
        
    
    
        
        
