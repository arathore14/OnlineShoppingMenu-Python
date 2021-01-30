#--------------------------------------------------------------------------
# Class: IT 209-001
 
# Lab Assignment #4: Baggage Container Class Definition Program

# Purpose: To create a Enhanced Program to define container class

# Author: Amanpreet Rathore

# Date: 09/25/2019
#--------------------------------------------------------------------------


class InvItem():

    def __init__(self, itemName):
        """Purpose of this __init Function is to intialize all the attributes of this class.
        Setting and Assigning variables to create attributes. """
        self.itemName = itemName

class Baggage():

    def __init__(self, inventory, capacity, allowed_items):
        """Purpose of this __init Function is to intialize all the attributes of this class.
        Setting and Assigning variables to create attributes. """
        self.inventory = [ ]
        self.capacity >= 5
        if self.capacity >= 5:
            return True,"added"
        else:
            return False, "capacity full"
        self.allowed_items = {"pen", "book", "coat", "umbrella", "gloves", "jacket", "food", "wallet"
            ,"keys", "laptop", "phone", "chapstick", "spectacles", "calculator"} 
                    
    def print_items(self):
        """Purpose of this Function is to structure the attributes in a proper output statement.
        Simple concatenation and casting is used to structure this. """
        for b in self.inventory():
            print(b)

    def add_items(self, i_obj, backpack):
        """Purpose of this Function is to add items """
        for i in self.allowed_items:
            if InvItem not in self.inventory:
                self.inventory.append
                return True, "added"
            else:
                return False, "included"

    def remove_item(self, i_obj, backpack):
        """Purpose of this Function is to remove items """
        for i in self.allowed_items:
            if InvItem not in self.inventory:
                self.inventory.delete
                return True, "deleted"
            else:
                return False, "not found"

    def has_item(self, i_obj, backpack):
        """Purpose of this Function is to check to see if the items are in the list """
        if t_obj in self.inventory:
            return True, "b_obj found"
        else:
            return False, "b_obj not found"



# 5 InventoryItem objects:

It1 = InvItem("book")
It2 = InvItem("umbrella")
It3 = InvItem("coat")
It1 = InvItem("pen")
It2 = InvItem("cap")


#2 Baggage objects:

backpack = Baggage(inventory, capacity, allowed_items )
satchel = Baggage(inventory, capacity, allowed_items )


