

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
                

