#--------------------------------------------------------------------------
# Class: IT 209-001
 
# Assignment #6: Extending the Dictionary Class

# Purpose: To create a program by  extending
#          the ‘dictionary’ class by adding a new subclass and four methods.

# Author: Amanpreet Rathore

# Date: 10/29/2019
#--------------------------------------------------------------------------

# Build the basic dictionary with this list:
movies = [[1965, 'The Sound of Music', 'musical'],
          [1972, 'The Godfather', 'drama'],
          [1977, 'Annie Hall', 'comedy'],
          [1990, 'Dances with Wolves', 'western'],
          [1993, 'Unforgiven', 'western'],
          [2011, 'The Artist', 'comedy'],
          [2012, 'Argo', 'historical'],
          [2013, '12 Years a Slave', 'drama'],
          [2014, 'Birdman', 'comedy'],
          [2015, 'Spotlight', 'drama'],
          [1994, 'Forrest Gump', 'comedy'],
          [1995, 'Braveheart', 'historical'],
          [1997, 'Titanic', 'historical'],
          [1998, 'Shakespeare in Love', 'comedy'],
          [2000, 'Gladiator', 'action'],
          [2002, 'Chicago', 'musical'],
          [2009, 'The Hurt Locker','action'],
          [2010, 'The Kings Speech', 'historical'],          
          [2016, 'Moonlight', 'drama'],
          [2017, 'The Shape of Water', 'fantasy']]

# Add to the dictionary using this list as input to the method:
movies1 = [[1939, 'Gone with the Wind', 'historical'],
           [1976, 'Rocky', 'drama'],
           [1985, 'Amadeus', 'historical'],
           [1980, 'Ordinary People', 'drama'],
           [1992, 'The Silence of the Lambs', 'suspense'],
           [1962, 'West Side Story', 'musical'],
           [1994, 'Shindlers List', 'historical'],
           [1971, 'Patton', 'historical'],
           [2019, 'Green Book', 'historical']]

class dict():
    dict=[]
    for m in movies:
        dict.append(m)

class NewDict(dict):
        
    def validList(self):
        for i in self:
            if not isinstance (i, list):
                return False, "Error Input Invalid"
        return True, None
    
    def displaysorted( D, R, B ): 
       if l1[0] == True:
            if not isinstance (D, R, B):
                print(D, " = Default Display List")
                return dict.sort()
            else:
                return True, dict
                print(D, " = Default Display List")
                return dict.sort()
            if R:
                print(R, " = return list")
                return dict.sort()
            elif B:
                print(B, " = Both Display and Return List")
                return dict.sort()
                  
    def addfromlist(list):
        l1 = self.validList()
        if l1[0] == True:
            if not isinstance (self, list):
                return False, "not a list"
            else:
                movies1[0]=[movies1[1], movies1[2]]
                for m in movies:
                    list.append(movies1)
                    dict.append(list)
                    return True, dict

    def retrieve(list):
        l1 = self.validList()
        if l1[0] == True:
            if not isinstance (self, list):
                return False, "not a list"
            elif l1 not in dict:
                return "Not found"
            else:
                return True, list, list[0]

    def merge(dict):
        l1 = self.validList()
        if l1[0] == True:
            if not isinstance (self, list):
                return False, "not in dict"     
            for i in dict:
                if i[0] not in dict:
                    return False, "Invalid Input"
                else:
                    dupes=[]
                    dupes.append(1)
                    return True, dupes
                    
                      



# Test Code to run against the extended Dictionary: --------------

MD = NewDict()
for m in movies:
    MD[m[0]] = [m[1], m[2]]
print('\n\nMovie dictionary built from a list follows...')

for md in MD:
    print(md, MD[md])

print('\n\nMovie dictionary printed using "displaysorted()" method...')
MD.displaysorted()

print('\n\nThe dictionary via "displaySorted("B")" method...')
L1 = MD.displaysorted('B')

print('\n\n')
L2 = MD.displaysorted('L')

print('\n\n"movies1" list..."')
for m in movies1:
    print(m)
    
print('\n\nThe dictionary after "MD.addfromlist(movies1)"...')
MD.addfromlist(movies1)
for m in MD:
    print(m, MD[m])

print('\n\nMovie dictionary printed using "displaysorted()" method...')
MD.displaysorted()

print('\n\nThe list returned after "MD.retrieve([1939, 1960, 1961, 1976, 1992, 2000])"...')
x, L5 = MD.retrieve([1939, 1960, 1961, 1976, 1992, 2000])
for n in L5:
    print(n)

input('Hit "Enter" to end program')




