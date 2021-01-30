##Program name: IT209_A*.py
##Purpose: IT_209 Assignment 9


##------------------------------------------------------------##---------------------------------------------------------##            
##------------------------------------------------------Person Class-----------------------------------------------------##
##------------------------------------------------------------##---------------------------------------------------------##


class Person (object):
    totalEnrollment = 0
    def __init__(self,a_num, name, address, telephone, email):
        self.a_num= a_num
        self.name = name
        self.address = address
        self.telephone = telephone
        self.email = email
        
    def samePerson(self, stud_obj):
        if self.a_num == stud_obj.a_num and self.name == stud_obj.name:     
            return True
        if not isinstance(stud_obj, Student):
            return False
        
    def __str__(self):
        return("Person: " +' '+ self.a_num +' '+  self.name + ' '+  self.address)
    
##------------------------------------------------------------##---------------------------------------------------------##            
##------------------------------------------------------Student Class----------------------------------------------------##
##------------------------------------------------------------##---------------------------------------------------------##
class Student(Person):
    stud_list= []
    def __init__(self, gnum, name, address, telephone, email, status, major, enrolled, credits, qpoints):
            super().__init__(gnum, name, address, telephone, email)
            self.status = status
            self.major = major
            self.enrolled = enrolled
            self.credits = credits
            self.qpoints = qpoints
        
    def __str__(self):
        return (super().__str__( )) + str(self.status) +  str(self.major) + ', ' + str(self.credits)+ ', ' + 'gpa: ' + '{:.2f}'.format(self.gpa())

    def gpa(self):
        try:
            return(self.qpoints/self.credits)
        except ZeroDivisionError:
            return 0

    def isEnrolled(self):
        if self.enrolled =='y':
            return True
        else: 
            return False

    def status(self):
        if self.credits >= 90:
            return 'Senior'
        elif self.credits>= 60:
            return 'Junior'
        elif self.credits>= 30:
            return 'Sophmore'
        else:
            return 'Freshman'


    def setMajor(self, major):
        self.major = major
        return True

    
##    def getInfo(self):
##        return((name) + ' ' + (address) + ' ' + (telephone) + " " + (email) + " " + (status) + " "
##               + (major) + " " + (enrolled))
##    
##    def setInfo(self, name, address, telephone, email, status, major, enrolled):
##        name= input("Enter name: ")
##        address = input("Enter address: ")
##        telephone = input("Enter telephone: ")
##        email = input("Enter email: ")
##        status = input("Enter status: ")
##        major = input("Enter major: ")
##        enrolled = input("Enrolled? (y/n): ")
##        return((name) + ' ' + (address) + ' ' + (telephone) + " " + (email) + " " + (status) + " "
##               + (major) + " " + (enrolled))


    def setName(self):
        name = input("Re-Enter Name: ")
        return name
    
    def setAddress(self):
        name = input("Re-Enter Address: ")
        return Address

    def setTelephone(self):
        telephone = input("Re-Enter Telephone: ")
        return telephone
    
    def setEmail(self):
        email = input("Re-Enter Email: ")
        return email
    
    def setStatus(self):
        status = input("Re-Enter status: ")
        return status
    
    def setMajor(self):
        major = input("Re-Enter major: ")
        return major
    
    def setEnrolled(self):
        enrolled = input("Please confirm enrollment: ")
        return enrolled


    
##------------------------------------------------------------##---------------------------------------------------------##            
##------------------------------------------------------Faculty Class----------------------------------------------------##
##------------------------------------------------------------##---------------------------------------------------------## 

class Faculty (Person):
    
    def __init__(self, a_num, name, address, telephone, email, rank, active, teach_load, specialty, funding):
        super().__init__(gnum, name, address, telephone, email)
        self.rank = rank
        self.active = active
        self.teach_load = teach_load
        self.specialty = specialty
        self.funding = funding
        

    def __str__(self):
        return ('Faculty: '  + (super().__str__()) + ', ' + str(self.rank) +', ' + str(self.specialty))
    
    def setName(self):
        name = input("Re-Enter Name: ")
        return name
    
    def setAddress(self):
        name = input("Re-Enter Address: ")
        return Address

    def setTelephone(self):
        telephone = input("Re-Enter Telephone: ")
        return telephone
    
    def setEmail(self):
        email = input("Re-Enter Email: ")
        return email
    
    def setStatus(self):
        status = input("Re-Enter status: ")
        return status
    
    def setMajor(self):
        major = input("Re-Enter major: ")
        return major
    
    def setEnrolled(self):
        enrolled = input("Please confirm Enrollment: ")
        return enrolled
##------------------------------------------------------------##---------------------------------------------------------##            
##----------------------------------------------------Administration Class-----------------------------------------------##
##------------------------------------------------------------##---------------------------------------------------------## 

class Administration(Person):
    def __init__(self, a_num, name, address, telephone, email, active, role):
        super().__init__(self, a_num, name, address, telephone, email)
        self.active = active
        self.role= role   

    def __str__(self):
        return ('Administration: '  + (super().__str__()) + ', ' + str(self.active) +', ' + str(self.role))

    
    def setName(self):
        name = input("Re-Enter Name: ")
        return name
    
    def setAddress(self):
        name = input("Re-Enter Address: ")
        return Address

    def setTelephone(self):
        telephone = input("Re-Enter Telephone: ")
        return telephone
    
    def setEmail(self):
        email = input("Re-Enter Email: ")
        return email
    
    def setStatus(self):
        status = input("Re-Enter status: ")
        return status
    
    def setMajor(self):
        major = input("Re-Enter major: ")
        return major
    
    def setEnrolled(self):
        enrolled = input("Please confirm enrollment: ")
        return enrolled   

##------------------------------------------------------------##---------------------------------------------------------##            
##----------------------------------------------------University Class---------------------------------------------------##
##------------------------------------------------------------##---------------------------------------------------------## 

class University(list):
    d_list=["Math Department", "Engineering", "CHHS', 'College of Health and Human Sevrices"] #hardcode
    def __init__(self, l):
        for i in self :
            if i not in l:
                l.append(i)
                return True, "Success"

    def append(self, d_obj):
        if d_obj not in self:
            super().append(d_obj)
            return True, "Request is successful"
        else:
            return False, "Request Failed!! Duplicate"

    def insert(self, d_obj):
        if d_obj  in self:
            return False, "Duplicate"
        else:
            super().insert(index, d_obj)
            return True, "Successful"

##------------------------------------------------------------##---------------------------------------------------------##            
##----------------------------------------------------Department Class---------------------------------------------------##
##------------------------------------------------------------##---------------------------------------------------------## 
    
class Department(University):
    univ_studs = 0
    def __init__(self,capacity, minGPA):
        self.capacity = capacity
        self.d_name= ["Math Department", "Engineering", "CHHS"]
        self.minGPA = minGPA
        self.num_studs = 0
        Department.univ_studs +=1
        self.avgGPA = 0
        self.s_roster =[s1]
        self.f_roster =[]
        self.a_roster=[]
        
##    def __str__(self):
##        ( "Name: " + ' ' + str(self.d_name) + " " +
##                "the capacity in that department is: " + ' ' + str(self.capacity) + ' ' + "with number of students")

        
    def addStudent(self, stud_obj):
        
        if  self.isQualified(stud_obj)[0] == True:
            self.s_roster.append(stud_obj)
            self.num_studs +=1
            Department.univ_studs +=1
            for s in self.s_roster:
                self.avgGPA += s.gpa()
                self.avgGPA = round(self.avgGPA / len(self.roster),2)
            stud_obj.setMajor(self.d_code)
            return True, self.isQualified(stud_obj)[1]
        return False, self.isQualified(stud_obj)[1]


                
    def addFaculty(self, f_obj):
        if not isinstance(f_obj, Faculty):
            return False, "Error! Trying to add wrong person"
        else:
            self.f_roster.append(f_obj)
            return True, "Faculty Member Sccuessfully Added!"
        

    def addAdministration(self, a_obj):
        if not isinstance(f_obj, Administration):
            return False, "Error! Trying to add wrong person"
        else:
            self.a_roster.append(a_obj)
            return True, "Administrator Sccuessfully Added!"

    def findPerson(self, a_num):
        for p in self.s_roster:
            if p[0] != a_num:
                return None
            else:
                return p
        for p in self.f_roster:
            if p[0] != a_num:
                return None
            else:
                return p
        for p in self.a_roster:
            if p[0] != a_num:
                return None
            else:
                return p    
              
            
    def isQualified(self, stud_obj):
        if self.num_studs >= self.capacity:
            return (False, "The maximum capacity reached for this department")    
        if not stud_obj.isEnrolled():
            return (False, "The student is not enrolled")
        if stud_obj.gpa() < self.minGPA:
            return (False, "The GPA requirement is not met")
        if len(self.s_roster) >0:
            for i in self.s_roster:
                if i.samePerson(stud_obj)== True:
                    return (False, "The Person is same student")
        
        return (True, "The student has been successfully added")
                
    def printRoster(self):
        ##If statement bc we are searching one student at a time      
        for s in self.s_roster:
            print(s)
        for f in self.f_roster:
            print(f)
        for a in self.a_roster:
            print(a)

##------------------------------------------------------------##---------------------------------------------------------##            
##----------------------------------------------------Course Class-------------------------------------------------------##
##------------------------------------------------------------##---------------------------------------------------------## 

class Course():
    c_list=[109, 209, 309, 469]
    def __init__(self, descr, code, number):
        self.descr =descr
        self.code = code
        self.number = number
        self.Title(number)

    """def isValid(self, obj):
        course_list=["
        ##NEED TO DISCUSS: have a course list, make a list check course list """

    def Title(self, number):
        try:
            if number == 109:
                return("Introduction to Computer Programming")
            if number== 209:
                return("Introduction to Object Oriented Programming")
            if number == 102:
                return ("Discrete Structures")
        except:
            return ("Error! Please enter the appropriate number.")

    def __str__(self):
        return( "Course:"+" "+ self.code +""+ self.number +""+ self.title)
        
    def getDescr(self):
        return self.descr
    def setDescr(self, d_obj):
        self.descr=d_obj
        return self.descr
    
    def getCode(self):
        return self.code
    def setCode(self, c_obj):
        self.code =c_obj
        return self.code

    def getnumber(self):
        return( self.number)
    
    def setNumber(self):
        number=int(input("Enter Course Number: "))
        return number 
        

##------------------------------------------------------------##---------------------------------------------------------##            
##----------------------------------------------------Job Class-------------------------------------------------------##
##------------------------------------------------------------##---------------------------------------------------------## 

class Job():
    def __init__(self, typee, descr, building, hours):
        self.typee= typee
        self.descr= descr
        self.build= building
        self.hours= hours

    def __str__(self):
        return( "Job type: "+self.typee+" Job Description: " + self.descr)

    def checkHours(self, obj):
        if  isinstance(Student, obj) and self.hours >40:
            return("Full-time students can't work more than 40 hours per week")
        return(self.hours)##add print
        

    ##def changeJob(self. j_job):
       ## self.ty
    def printJob(self):
        return( "Job type: "+self.typee+" Job Description: " + self.descr)
    
##------------------------------------------------------------##---------------------------------------------------------##            
##----------------------------------------------------Session+ Class-------------------------------------------------------##
##------------------------------------------------------------##---------------------------------------------------------## 

"""import os, datetime

class ATMSession:     # ATMSession - on object per ATM user session
    sessionNo = 1
    def __init__(self, cardno, pin, ATM_ID):
        self.cardno = cardno
        self.pin = pin
        self.ATM_ID = ATM_ID
        self.activityLog = [ ]  # holds log of all activities for this session
        self.sessionNum = ATMSession.sessionNo
        ATMSession.sessionNo += 1

    def addLog (self, event):
        self.activityLog.append(event)

    def __str__(self):
        ret = self.ATM_ID + '\nSession number: ' + str(self.sessionNum) + \
              '\nCard number: ' + self.cardno + '\n'
        for log in self.activityLog:
            ret = ret + str(log[0]) + ' ' + str(log[1]) + '\n'    
        return ret """
#####-----------------------------------------Live Code---------------------------------------------------#####

print("\n\tWelcome to Aim University\n")
University("Math Department")
University("IT Department")
while True:
    try:
        select=(input("Would you like to search a person or add a person  or exit? (s-search or a-add): "))
        if select == 's':
            pick=input("Would you like to search s-Student, f-Faculty or a-Administration: ")
            if pick == 's':
                a_num=input("Enter an a_num: ")
                
                for d in University.d_list:
                    x=d.findPerson(a_num)
                    p =None
                    if x is not None:
                        p = x
                        print(x, p)
                
                    break
                        
                
                Student.printRoster()
                Job.printJob()
                #print club
            if pick=='f':
                Faculty.printRoster()
                Job.printJob()
            if pick =='a':
                Administration.printRoster()
                Job.printJob()

                
        if select == "a":
            pick=input("Would you like to search s-Student, f-Faculty or a-Administration: ")
            if pick == 's':
                print("  \n\tNew Student Application:  \n")
                name = input("Enter Your Name: ")
                Student.setName(name)
                
                Address = input("Enter Your address: ")
                Student.setAddress(Address)
                
                telephone = input("Enter Your TelePhone: ")
                Student.setTelephone(telephone)
                
                email = input("Enter Your Email: ")
                Student.setEmail(email)

                status = input("Enter Your status: ")
                Student.setStatus(status)
                
                major = input("Enter Your major: ")
                Student.setMajor(major)

                number=int(input("Enter Course Number: "))
                Course.setNumber(number)
                
                enrolled = input("Do you wish to enroll in this course?: ")
                Student.setEnrolled(enrolled)
                
                print("New Student: ", name, Address, telephone, email, status, major, enrolled)

                
##                Student.setInfo(name, address, telephone, email, status, major, enrolled)
##                print(name, address, telephone, email, status, major, enrolled)
##                Student.getInfo(self)
##                Student.setA_Num(A_Num)
##                Student.setTelephone(Telephone)
##                Student.setEmail(Email)
##
##               
##                Student.stud_list.append(name, A_Num, Telephone, Email)


            
            if pick == 'f':
                print("  \n\tNew Faculty Application:  \n")
                name = input("Enter Your Name: ")
                Student.setName(name)
                
                Address = input("Enter Your address: ")
                Student.setAddress(Address)
                
                telephone = input("Enter Your Phone Number: ")
                Student.setTelephone(telephone)
                
                email = input("Enter Your Email: ")
                Student.setEmail(email)

                status = input("Enter Your status: ")
                Student.setStatus(status)
                
                major = input("Enter Your major: ")
                Student.setMajor(major)
                
                enrolled = input("Enter Your enrolled: ")
                Student.setEnrolled(enrolled)
                
                print("New Faculty: ", name, Address, telephone, email, status, major, enrolled)
                
            if pick == 'a':
                print("  \n\tNew Administration Application:  \n")
                name = input("Enter Your Name: ")
                Student.setName(name)
                
                Address = input("Enter Your address: ")
                Student.setAddress(Address)
                
                telephone = input("Enter Your Phone Number: ")
                Student.setTelephone(telephone)
                
                email = input("Enter Your Email: ")
                Student.setEmail(email)

                status = input("Enter Your status: ")
                Student.setStatus(status)
                
                major = input("Enter Your major: ")
                Student.setMajor(major)
                
                enrolled = input("Enter Your enrolled: ")
                Student.setEnrolled(enrolled)
                
                print("New Administrator: ", name, Address, telephone, email, status, major, enrolled)
                
        if select == "exit" or "Exit":
            break
    except:
        print("Error!! ")
    select=(input("Would you like to search a person or add a person  or exit? (s-search or a-add): "))



    
s1 = Student('G34568', 'David Miller', address='xyz road, north st. leesburg, VA- 20176', telephone= '5716583482', email= 'xyz@gmu.edu',
             status = 'sophomore', major = 'Hist', enrolled = 'y', credits = 30, qpoints = 90)           
s2 = Student('G21345', 'Sonia Fillmore', address='xyz road, north st. leesburg, VA- 20176', telephone= '5714399524', email=  'xyz@gmu.edu',
             status = 'senior', major = 'Math', enrolled = 'y', credits = 90, qpoints = 31)
s3 = Student('G42156', 'Chris Squire', address='xyz road, north st. leesburg, VA- 20176', telephone= '5714369422', email= 'xyz@gmu.edu',
             status = 'sophomore', major = 'Musc', enrolled = 'y', credits = 45, qpoints = 160)           
s4 = Student('G10928', 'Tal wilkenfeld', address='xyz road, north st. leesburg, VA- 20176', telephone='5715669482', email=  'xyz@gmu.edu',
             status = 'junior', major = 'ARTS', enrolled = 'y', credits = 70, qpoints = 225)
s5 = Student('G22157', 'Larry Graham', address='xyz road, north st. leesburg, VA- 20176', telephone='5715899482', email= 'xyz@gmu.edu',
             status = 'senior', major = 'CHHS', enrolled = 'y', credits = 105, qpoints = 290)           
s6 = Student('G31345', 'John Entwistle', address='xyz road, north st. leesburg, VA- 20176', telephone='5713663482', email= 'xyz@gmu.edu',
             status = 'freshman', major = 'CSci', enrolled = 'y', credits = 15, qpoints = 35)
s7 = Student('G44568', 'Esperanza Spalding', address='xyz road, north st. leesburg, VA- 20176', telephone= '5712451234', email= 'xyz@gmu.edu',
             status = 'junior', major = 'ENGR', enrolled = 'y', credits = 65, qpoints = 250)           
s8 = Student('G55345', 'Tim Bogert',address='xyz road, north st. leesburg, VA- 20176', telephone= '5712453482', email= 'xyz@gmu.edu',
             status = 'sophomore', major = 'Hist', enrolled = 'y', credits = 45, qpoints = 120)

s9 = Student('G66113', 'Gordon Sumner',address='xyz road, north st. leesburg, VA- 20176',telephone= '5712453482', email= 'xyz@gmu.edu',
             status = 'freshman', major = 'Musc', enrolled = 'y', credits = 15, qpoints = 45)           
s10 = Student('G11311', 'Paul McCartney', address='xyz road, north st. leesburg, VA- 20176', telephone='5715253482' , email= 'xyz@gmu.edu',
              status = 'senior', major = 'ARTS', enrolled = 'y', credits = 110, qpoints = 275)
s11 = Student('G22111', 'Elizabeth Smythe', address='xyz road, north st. leesburg, VA- 20176', telephone= '5715333482', email= 'xyz@gmu.edu',
              status = 'junior', major = 'ENGR', enrolled = 'y', credits = 85, qpoints = 250)
        


##print('List of Students created: ')
##print('s1=  ',s1)
##print('s2=  ',s2)
##print('s3=  ',s3)
##print('s4=  ',s4)      
##print('s5=  ',s5)
##print('s6=  ',s6)      
##print('s7=  ',s7)
##print('s8=  ',s8)
##print('s9=  ', s9)
##print('s10= ',s10)


input("Hit Enter to quit")




"""_init__:

a_num: (-1) You should Ensure that the a_num is correctly created and not be constant:
n = str(Student.totalEnrollment)
if len(n) == 1:
self.a_num = 'G0000' + n
elif len(n) == 2:
self.a_num = 'G000' + n
elif len(n) == 3:
self.a_num = 'G00' + n
elif len(n) == 4:
self.a_num = 'G0' + n
else:
self.a_num = 'G' + n"""
      
input("Hit Enter to quit")


