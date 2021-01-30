## A1- Reviewing & Exercising Python
## Amanpreet Rathore
## Date: 09/04/2019


#"Open the file"
infile = "A1input.txt"
fi=open(infile,"r")
wholeFile = fi.readlines()

items=[ ]

        
def createItems():
    """"This func reads the file and iterates through it"""
    
    for b in wholeFile:
        if len(b) > 4:
            x= b.split(",")
            x[0] = x[0].strip()
            x[1] = x[1].strip()
            x[2] = x[2].strip()
            x[3] = x[3].strip()
            items.append(x)

    return items

createItems()

def displayItems(items):
    """"This func reads the reads through it"""
    for i in items:

        print(i)

displayItems(items)
print("\n")
def book(items):
    """"This func is for book category"""
    list1 = [ ]
    for i in items:
        if i[1] == 'book':
           list1.append(i)
                

        #print(list1)
    for i in list1:
        print(i[0],i[1],i[2],i[3])
        
    #print('\n')
    #print("Book Category List: ")

book(items)
   
    #print(" ")
  
def cloth(items):
    """"This func is for cloth category"""
    list1 = [ ]
    for i in items:
        if i[1] == 'cloth':
            list1.append(i)

    for i in list1:
        print(i[0],i[1],i[2],i[3])
    #print('\n')        
    #print(list1)
cloth(items)

##print("Clothing Category List: ")


    #print(" ")
    
def elect(items):
    """"This func is for elect category"""
    list1 = [ ]
    for i in items:
        if i[1] == 'elect':
            list1.append(i)

    for i in list1:
        print(i[0],i[1],i[2],i[3])
        
   # print('\n')        
    #print(list1)
elect(items)
#print("Electronics Category List: ")
##elect(items)

#print(" ")

def food(items):
    """"This func is for food category"""
    list1 = [ ]
    for i in items:
        if i[1] == 'food':
            list1.append(i)

    for i in list1:
        print(i[0],i[1],i[2],i[3])
    #print('\n')        
    #print(list1)
food(items)
#print("Food Category List: ")
##food(items)
##
print('\n')
def displayItems(items):

    """"This func is for display category in format"""

    for i in items:

        print("{0:7s} {1:6s} {2:45s} {3:8.2f}".format(i[0], i[1], i[2], float(i[3])))

displayItems(items)

def formItems(items):

    """"This func is for build the items"""

    Dic1={}

    for x in items:

        if x[1] not in Dic1:

            Dic1[x[1]]=[[x[0],x[2], float(x[3])]]

        else:

            Dic1[x[1]].append([x[0],x[2], float(x[3])])

    return Dic1


def makeFile(items):

    """"This func is for write whats in the file"""

    f=open('RathoreAA1output.txt','w') ##with open('RathoreAoutput.txt','w') as f
    for i in items:
        f.write('\n')
        for n in i:
            f.write(n)
 
        
item123 = createItems()

makeFile(items)


AB=formItems(item123)
makeFile(AB)




fi.close()
