## LA1- Reviewing & Exercising Python
## Amanpreet Rathore
## Date: 08/28/2019


#"Open the file"
infile = "A1input.txt"
fi=open(infile,"r")
wholeFile = fi.readlines()

        
def loadItems():
    itemList=[ ]
    for b in wholeFile:
        if len(b) > 4:
            x= b.split(",")
            x[0] = x[0].strip()
            x[1] = x[1].strip()
            x[2] = x[2].strip()
            x[3] = x[3].strip()
            itemList.append(x)

    for b in itemList:
        print(b)

    print("")
    
    def book(itemList):
        list1 = [ ]
        for i in itemList:
            if i[1] == 'book':
                list1.append(i)
                
        print(list1)
        return itemList
    print("Book Category List: ")
    book(itemList)
    
    print(" ")
    
    def cloth(itemList):
        list1 = [ ]
        for i in itemList:
            if i[1] == 'cloth':
                list1.append(i)
                
        print(list1)
        return itemList
    print("Clothing Category List: ")
    cloth(itemList)

    print(" ")
    
    def elect(itemList):
        list1 = [ ]
        for i in itemList:
            if i[1] == 'elect':
                list1.append(i)
                
        print(list1)
        return itemList
    print("Electronics Category List: ")
    elect(itemList)

    print(" ")

    def food(itemList):
        list1 = [ ]
        for i in itemList:
            if i[1] == 'food':
                list1.append(i)
                
        print(list1)
        return itemList
    print("Food Category List: ")
    food(itemList)

itemList = loadItems()

fi.close()
    

##def displayItems(itemList):
##    for i in itemList:
##        print(i)
##displayItems(itemList)

##def buildDict(itemList):
##    dict = {itemList}
####    for i in itemList:
####        dict.append(i)
##
##    i = len(dict)
##
##    for k in range(i, 0):
##        print(dict[k])
        
        
##DS = buildDict(itemList)
##
##print(DS)



##for b in itemList:
##    print(b)



    

#for n in wholeFile(n[0]) == "book":
     #itemList.append(x)
    

    
##for n in range(0, len(itemList)):
##        print('\t\t\t {0:25s} \t {1:25s} \t {2:25s} \t ${3:8.2f}'.format(itemList[n][0], itemList[n][1], itemList[n][2], itemList[n][3]))





    
