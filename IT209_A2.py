#--------------------------------------------------------------------------
# Class: IT 209-001
 
# Assignment #2: Student Class Definition

# Purpose: To create a program to define class to model STUDENT attributes

# Author: Amanpreet Rathore

# Date: 09/14/2019
#--------------------------------------------------------------------------

class Student(object):
    """Student Class- Creates objects based on Students' characteristics
    ----------------------------------------------------------------------"""
    totalEnrollment = 0
    enrolled = "y"
    #totalEnrollment +=1
    def __init__ (self, name, g_num, major= "IST", enrolled="y", credits=0, qpoints=0):
        """Purpose of this __init Function is to intialize all the attributes of this class.
        Setting and Assigning variables to create attributes. """
        Student.totalEnrollment += 1
        self.name = str(name)
        self.g_num = str(g_num)
        #self.g_num = "G"+"0000" + str(g_num)
        self.g_num = "G" + "0000" + str(Student.totalEnrollment +1)
        #self.g_num = Student.totalEnrollment
        self.major = str(major) #{“Acctg”, “Art”, “CSci”, “Hist”, “IST”, “Math”, “Physics”}
        self.enrolled = enrolled #{“y”, “n”}
        self.credits = float(credits)
        self.qpoints = float(qpoints)

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
        
    def sameStudent(self, s_obj):
        """Purpose of this Function is to determine if the self student's g_num and name is 
        equilvalent to the Student object by returning the boolean value of True or False."""
        if self.g_num == s_obj.g_num and self.name == s_obj.name:
            return True
        else:
            return False
        
##        if self == s_obj:           # Is the input object me? If yes, short cut to 'True'
##            return True
##        if not isinstance(s_obj, Student):
##            return False
##        return(self.g_num == s_obj.g_num and self.name == s_obj.name)
    
    def __str__(self):
        """Purpose of this Function is to structure the attributes in a proper output statement.
        Simple concatenation and casting is used to structure this. """
        return("Total Enrollment= " + str(self.totalEnrollment) + ", GNumber= " + str(self.g_num)
        + ", Name = " + str(self.name) + ", Major = " + str(self.major) + ", Enrolled = " + self.enrolled
        + ", Credits = " + str(self.credits) + ", qpoints = " + str(self.qpoints))

        #return ("GNumber: " + str(self.g_num) + " " +  )

print('\nStart of A2 Student Class Program \n')

s1 = Student('David Miller', g_num= "G" + "0000" + str(Student.totalEnrollment), major = 'Hist', enrolled = 'y', credits = 0, qpoints = 0)
print('s1 = ', s1)

s2 = Student('Sonia Fillmore', g_num= "G" + "0000" + str(Student.totalEnrollment), major = 'Math',
      enrolled = 'y', credits = 90, qpoints = 315)
print('s2 = ', s2)


s3 = Student('A. Einstein', g_num= "G" + "0000" + str(Student.totalEnrollment), major = 'Phys',
      enrolled = 'y', credits = 0, qpoints = 0)
print('s3 = ', s3)


s4 = Student('W. A. Mozart', g_num= "G" + "0000" + str(Student.totalEnrollment), major = 'Mus',
      enrolled = 'n', credits = 29, qpoints = 105)
print('s4 = ', s4)

s5 = Student('Sonia Fillmore', g_num= "G" + "0000" + str(Student.totalEnrollment), major = 'CSci',
      enrolled = 'y', credits = 60, qpoints = 130)
s5.g_num = s2.g_num
print('s5 = ', s5)


s6 = Student('Pierre Renoir', g_num= "G" + "0000" + str(Student.totalEnrollment), major = 'Art',
     enrolled = 'y', credits = 120, qpoints = 315)
print('s6 = ', s6)



#What is TotalEnrollment?
print('\nTotal number of students: ', Student.totalEnrollment)

#What is GPA?
print('The gpa of ', s1.name, ' is ', s2.gpa())

#What is Status?
print('Class standing of ', s4.name, ' is ', s4.status())
print('Class standing of ', s2.name, ' is ', s2.status())

#Are Students Equal?
if s1.sameStudent(s2):
    print (s1.name, ' and ', s2.name, ' are the same student')
else:
    print (s1.name, ' and ', s2.name, ' are not the same student')
if s2.sameStudent(s5):
    print (s2.name, ' and ', s5.name, ' are the same student')
else:
    print (s2.name, ' and ', s5.name, ' are not the same student')

#Enrolled?   
if s1.isEnrolled() == True:
    print (s1.name, ' is currently enrolled')
elif s1.isEnrolled() == False:
    print (s1.name, ' is not currently enrolled')
if s4.isEnrolled() == True:
    print (s4.name, ' is currently enrolled')
elif s4.isEnrolled() == False:
    print (s4.name, ' is not currently enrolled')


print('\nEnd of A2 Student Class Program')



    



        
