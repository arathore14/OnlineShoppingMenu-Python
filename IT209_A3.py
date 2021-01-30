#--------------------------------------------------------------------------
# Class: IT 209-001
 
# Assignment #3: University Department Class Definition

# Purpose: Python program to define a class to model some characteristics of a
#          university Department using the STUDENT class

# Author: Amanpreet Rathore

# Date: 09/30/2019
#--------------------------------------------------------------------------


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




#DEPARTMENT CLASS______________

class Department():
    """Department Class- Creates Department objects based on Students' majors
    ----------------------------------------------------------------------"""
    univ_students = 0
    depart_Count = 0
    
    def __init__ (self, d_code = '', d_name = '', capacity = 0 , minGPA = 0.0):
        """Purpose of this __init Function IN THE DEPARTMENT CLASS is to intialize all the attributes of this class.
        Setting and Assigning variables to create attributes. """
        self.d_code = str(d_code)
        self.d_name = str(d_name)
        self.capacity = int(capacity)
        self.minGPA = float(minGPA)
        self.num_students = int(0)
        self.avgGPA = float(0.0)
        self.roster = []
        #addtional_methods
        self.qualified = True # isQualified Method set as "True"
        self.reason = ''
        Department.depart_Count += 1


    def addStudent (self, s_obj):
        """Purpose of this addStudent Function IN THE DEPARTMENT CLASS is to add students
        into the department if the requirements are met"""
        if not s_obj :
            if not isinstance (self, Student):
                return False, "Invalid Object Type"
        else:
            self.qualified, self.reason = self.isQualified(s_obj)
            #self.reason = self.isQualified(s_obj)
            
            if self.qualified:
                Department.depart_Count += 1
                self.num_students += 1
                self.roster.append(s_obj)
                s_obj.major = self.d_name
                self.Average()
            else:
                return False, "Not Qualified in Major Department"
            return True, "Student has been Added to Major"

##        if self == s_obj:           # Is the input object me? If yes, short cut to 'True'
##            return True
##        if not isinstance(s_obj, Student):
##            return False
##        return(self.g_num == s_obj.g_num and self.name == s_obj.name)
        
    def isQualified(self, s_obj):
        """Purpose of this isQualified Function IN THE DEPARTMENT CLASS is to see if the students are qualified
        into the department if the requirements are met"""
        #studentCapacity
        if self.num_students >= self.capacity:
            return (False, "NOT QUALIFIED! Capacity Filled")
        
        #studentEnrollment
        if not s_obj.isEnrolled():
            return (False, "NOT QUALIFIED! Student NOT Enrolled")
        
        #minimumGPA
        if s_obj.gpa() < self.minGPA:
            return (False, "NOT QUALIFIED! Invalid minGPA")
        
        else:
            if len(self.roster) > 0:
                
                for stud in self.roster:
                    if stud.sameStudent(s_obj.g_num, s_obj.name):
                        return (False, 'NOT QUALIFIED! Duplicate student detected in Department')
                    
        return (True,'Qualified Student')
    
    def Average(self):
        """Purpose of this Average Function IN THE DEPARTMENT CLASS is to calculate the students GPA """
        self.avgGPA = 0
        for stud in self.roster:
            self.avgGPA += stud.gpa()
            
        if len(self.roster) > 0 :
            GPA = ( (self.avgGPA) / (len(self.roster)) )
            
            return GPA
        
    def printRoster(self):
        """Purpose of this Function IN THE DEPARTMENT CLASS is to print all the data for students
        and display the list """
        print("\n\n List for Students and Departments: ", self.d_name)
        for stud in self.roster:
            print(stud)
        
        
    def __str__(self):
        """Purpose of this Function IN THE DEPARTMENT CLASS is to structure the attributes in a proper output statement.
        Simple concatenation and casting is used to structure this. """
        return ( "Department: " + str(self.d_name) + "-"
                 + "Capacity: " + str(self.capacity) + \
                    "- Number Of Students: "
                 + str(self.num_students)
                 + "- Avgerage GPA: " + str(self.minGPA))   
                





print('\nStart of Department and Student class demo **************')

s1 = Student('G34568', 'David Miller', status = 'sophomore', major = 'Hist',
      enrolled = 'y', credits = 30, qpoints = 90)           
s2 = Student('G21345', 'Sonia Fillmore', status = 'senior', major = 'Math',
      enrolled = 'y', credits = 90, qpoints = 315)
s3 = Student('G42156', 'Chris Squire', status = 'sophomore', major = 'Musc',
      enrolled = 'y', credits = 45, qpoints = 160)           
s4 = Student('G10928', 'Tal wilkenfeld', status = 'junior', major = 'ARTS',
      enrolled = 'y', credits = 70, qpoints = 225)
s5 = Student('G22157', 'Larry Graham', status = 'senior', major = 'CHHS',
      enrolled = 'y', credits = 105, qpoints = 290)           
s6 = Student('G31345', 'John Entwistle', status = 'freshman', major = 'CSci',
      enrolled = 'y', credits = 15, qpoints = 35)
s7 = Student('G44568', 'Esperanza Spalding', status = 'junior', major = 'ENGR',
      enrolled = 'y', credits = 65, qpoints = 250)           
s8 = Student('G55345', 'Tim Bogert', status = 'sophomore', major = 'Hist',
      enrolled = 'y', credits = 45, qpoints = 120)
s9 = Student('G66113', 'Gordon Sumner', status = 'freshman', major = 'Musc',
      enrolled = 'y', credits = 15, qpoints = 45)           
s10 = Student('G11311', 'Paul McCartney', status = 'senior', major = 'ARTS',
      enrolled = 'y', credits = 110, qpoints = 275)
s11 = Student('G22111', 'Elizabeth Smythe', status = 'junior', major = 'ENGR',
      enrolled = 'y', credits = 85, qpoints = 250)
s12 = Student('G31312', 'John McVie', status = 'sophomore', major = 'Hist',
      enrolled = 'y', credits = 45, qpoints = 120)
s13 = Student('G31312', 'Nawt Enrolled', status = 'sophomore', major = 'Hist',
      enrolled = 'n', credits = 45, qpoints = 120)
s14 = Student('G11112', 'Toolow G. Peyay', status = 'freshman', major = 'Undc',
      enrolled = 'y', credits = 20, qpoints = 38)           


print('List of Students created: ')
print('s2=  ',s1)
print('s2=  ',s2)
print('s3=  ',s3)
print('s4=  ',s4)      
print('s5=  ',s5)
print('s6=  ',s6)      
print('s7=  ',s7)
print('s8=  ',s8)
print('s9=  ', s9)
print('s10= ',s10)
print('s11= ',s11)
print('s12= ',s12)      
print('s13= ',s13)
print('s14= ',s14)      
d1 = Department('ENGR', 'Engineering', 5, 2.75)
d2 = Department('ARTS', 'Art and Architecture', 15, 2.0)
d3 = Department('CHHS', 'College of Health and Human Sevrices', 10, 2.5)
print('\n\nDepartments established:')
print(d1)
print(d2)
print(d3)
print('\n\nAdding s1 - s5 to ENGR Department- print Roster follows')
d1.addStudent(s1)      
d1.addStudent(s2)
d1.addStudent(s3)      
d1.addStudent(s4)
d1.addStudent(s5)
d1.printRoster()      

a, b = d1.addStudent(s6)
print('\nAttempting to add ', s6.name, ' to ', d1.d_code, ' - over capacity, ret values: ', a, b)
d1.printRoster()
      
print('\n\nAdding ', s6.name, ' and ', s7.name, ' to ', d2.d_code, ', printRoster follows: ')
d2.addStudent(s6)
d2.addStudent(s7)
d2.printRoster()

print('\n\nAdding ', s8.name, ' and ', s9.name, ' to ', d3.d_code, ', printRoster follows: ')
d3.addStudent(s8)
a, b = d3.addStudent(s9)
print('\nAttempting to add qualified student , ', s9.name, ' to ', d3.d_code, ', CHHS, return values; ', a, b)
d3.printRoster()

a, b = d3.addStudent(s14)
print('\n\nAttempting to add low GPA student ', s14.name, ', return values: ', a, b) 

a, b = d2.addStudent(s13)
print('\n\nAttempting to add non-enrolled student ', s13.name, ', return values: ', a, b) 

a, b = d3.addStudent(s8)
print('\n\nAttempting to add dupe student ', s8.name, ', return values: ', a, b) 

print('\n\nAdding s10 to ENGR, s11 to ARTS, s12 to CHHS, then print all 3 roster')
d1.addStudent(s10)
d2.addStudent(s11)
d3.addStudent(s12)

d1.printRoster()
d2.printRoster()
d3.printRoster()      
print('\n\n\n***** End of Student class demo **********')

    












    
    



        
