#STUDENT CLASS______________

class Student(object):
    """Student Class- Creates objects based on Students' characteristics
    ----------------------------------------------------------------------"""
    totalEnrollment = 0
    enrolled = "y"
    #totalEnrollment +=1
    def __init__ (self, name, g_num, status='', major= "IST", enrolled=" ", credits=0, qpoints=0):
        """Purpose of this __init Function is to intialize all the attributes of this class.
        Setting and Assigning variables to create attributes. """
        Student.totalEnrollment += 1
        self.name = str(name)
        self.g_num = str(g_num)
        #self.g_num = "G"+"0000" + str(g_num)
        self.g_num = "G" + "0000" + str(Student.totalEnrollment +1)
        #self.g_num = Student.totalEnrollment
        self.major = str(major) #{“Acctg”, “Art”, “CSci”, “Hist”, “IST”, “Math”, “Physics”}
        self.enrolled = enrolled.lower() #{“y”, “n”}
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
        if self.enrolled == 'y':
            return True
        elif self.enrolled == "n":
            return False

    def status(self):
        """Purpose of this Function is to return the status of the student by return the
        particular he/she is in. This can be Freshman, Sophomore, Junior or Senior """
        if self.credits >= 90:
            return ("senior")
            
        elif self.credits >=60:
            return ("junior")
            
        elif self.credits >= 30:
            return ("sophomore")
            
        elif self.credits < 30:
            #print("Freshman")
            return("freshman") 
        
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
