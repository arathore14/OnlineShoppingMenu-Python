#--------------------------------------------------------------------------
# Class: IT 209-001
 
# Assignment #5: Department/Student/Faculty Class Definition

# Purpose: To create a program to define class to model Person attributes

# Author: Amanpreet Rathore

# Date: 10/20/2019
#--------------------------------------------------------------------------

class Person():
    """Student Class- Creates objects based on Students' characteristics
    ----------------------------------------------------------------------"""
    def __init__ (self, name, g_num, address=" ",telephone=" ",email=" "):
        """Purpose of this __init Function is to intialize all the attributes of this class.
        Setting and Assigning variables to create attributes. """
        self.name = str(name)
        self.g_num = str(g_num)
        #self.g_num = "G"+"0000" + str(g_num)
        self.address = str(address) 
        self.telephone = str(telephone)
        self.email = str(email)

    def __str__(self):
        """Purpose of this Function is to structure the attributes in a proper output statement.
        Simple concatenation and casting is used to structure this. """
        return("Person= " + str(self.g_num) + str(self.name) + str(self.address))
    
    def samePerson(self,p_obj):
        """Purpose of this Function is to determine if the self student's g_num and name is 
        equilvalent to the Student object by returning the boolean value of True or False."""
        if self.g_num == p_obj.g_num and self.name == p_obj.name:
            return True
        else:
            return False

    #def printRoster("s" or "f"):
       # print("Person: ", Person + major + credits )
        
        
        

class Student(Person):
    """Student Class- Creates objects based on Students' characteristics
    ----------------------------------------------------------------------"""
    totalEnrollment = 0
    enrolled = "y"
    #totalEnrollment +=1
    def __init__ (self, name, g_num, major= "IST", enrolled="y", credits=0, qpoints=0, address=" ",telephone=" ",email=" "):
        """Purpose of this __init Function is to intialize all the attributes of this class.
        Setting and Assigning variables to create attributes. """
        Student.totalEnrollment += 1
        self.name = str(name)
        self.g_num = str(g_num)
        #self.g_num = "G"+"0000" + str(g_num)
        self.g_num = "G" + "0000" + str(Student.totalEnrollment +1)
        self.major = str(major) #{“Acctg”, “Art”, “CSci”, “Hist”, “IST”, “Math”, “Physics”}
        self.enrolled = enrolled #{“y”, “n”}
        self.credits = float(credits)
        self.qpoints = float(qpoints)
        self.address = str(address) 
        self.telephone = str(telephone)
        self.email = str(email)

    def getg_num(self):
        """Purpose of this Function is to generate the GNumber for each student,
        based of the number of studetns enrolled """
        #g_num = "G" + "0000" + str(Student.totalEnrollment)
        return self.g_num

    def gpa(self):
        """Purpose of this Function is to calculate the gpa
        for the student by using the qpoints and credits. """
        gpa = self.qpoints / self.credits
        return float(gpa)

    def isEnrolled(self):
        """Purpose of this Function is to return the boolean value of true
        or false if the student is currently enrolled. """
        if self.enrolled == "y":
            return True
        elif self.enrolled == "n":
            return False

    def status(self):
        """Purpose of this Function is to return the status of the student by return the
        particular he/she is in. This can be Freshman, Sophomore, Junior or Senior """
        if self.credits >= 90:
            return ("Senior")
            
        elif self.credits >=60:
            return ("Junior")
            
        elif self.credits >= 30:
            return ("Sophomore")
            
        elif self.credits < 30:
            #print("Freshman")
            return("Freshman")

    def __str__():
        return "Student: " + status + major  + (super().__str__)

    
class Faculty(Person):
    """Faculty Class- Creates objects based on Faculty' characteristics
    ----------------------------------------------------------------------"""
    def __init__ (self, name, g_num, address=" ",telephone=" ",email=" "):
        """Purpose of this __init Function is to intialize all the attributes of this class.
        Setting and Assigning variables to create attributes. """
        self.name = str(name)
        self.g_num = str(g_num)
        #self.g_num = "G"+"0000" + str(g_num)
        self.address = str(address) 
        self.telephone = str(telephone)
        self.email = str(email)
        self.rank = str(rank) #valid: {Professor, Associate Professor, Assistant Professor, Instructor}
        self.active = str(active)
        self.teach_load = int(teach_load)
        self.speciality = str(speciality)
        self.funding = int(funding)
                

    def rank(self):
        """Purpose of this Function is to generate the GNumber for each student,
        based of the number of studetns enrolled """
        #g_num = "G" + "0000" + str(Student.totalEnrollment)
        if rank in [Professor, Associate-Professor, Assistant-Professor, Instructor]:
            return True, "VALID"

    def active(self):
        """Purpose of this Function is to calculate the gpa
        for the student by using the qpoints and credits. """
        if active == "y":
            print("active member")
            
    def teach_load(self):
        """Purpose of this Function is to return the number
        of credit hours taught per year, range 0 to 24 . """
        num_credits= int(input("Enter the number of credits: "))
       

    def speciality(self):
        """Purpose of this Function is to return the status valid:
        {teaching, research, administration, combination}"""
        if rank in [ teaching, research, administration, combination ]:
            return True, "VALID"
        
    def funding(self):
        """Purpose of this Function is to return the dollar amount of supported research,
        range 0 to 10 million """
        fund= int(input("Enter the funding amount (range from 0 to 10 million): "))
        if fund < 0 and fund > 10000000:
            print("invalid amount")

        return fund

    def __str__():
        return "Faculty: " + rank + speciality


        
