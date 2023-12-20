
# Welcome to my self serve menu and retail store

class InventoryManagementSystem:
    def __init__(self): 
        self.inventory = { #self inventory is our selection of fruits,vegetables and dairy products
            'F01': ['Orange', 'Fruit', 2.99, 1000], #cell 15-17 are fruits and their prices
            'F02': ['Apple', 'Fruit', 1.99, 5000],
            'F03': ['Banana', 'Fruit', 1.5, 490],
            'D01': ['Milk', 'Dairy', 7.5, 500], #cell 18-20 are dairy products and its prices
            'D02': ['Cheese', 'Dairy', 15, 840],
            'D03': ['Yogurt', 'Dairy', 5.5, 700],
            'V01': ['Carrot', 'Vegetable', 3.8, 890], #cell 21-24 are all vegatables and its prices
            'V02': ['Celery', 'Vegetable', 3.99, 990],
            'V03': ['Bean', 'Vegetable', 4.5, 1500],
            'V04': ['Potato', 'Vegetable', 6, 1000],
        }

            #infront of the products are the product code starting from F01 to V04
            # F00 = fruits
            # D00 = dairy products
            # V00 = vegetables


    def displayMenu(self):
        print("Inventory Options:")
        print("1. Show all items")
        print("2. Look up the inventory")
        print("3. Add an item to the inventory")
        print("4. Change an item")
        print("5. Delete an item")
        print("6. Find items given category")
        print("7. Quit the program")
        
        #menu display function ^^^

    def displayInventory(self):
        print("\nCurrent Inventory:") 
        print("ID\tName\t\tCategory\tPrice\tQuantity")
        for item_id, details in self.inventory.items():
            print(f"{item_id}\t{details[0]}\t\t{details[1]}\t\t${details[2]:.2f}\t{details[3]}")

            #displaying inventory function ^^^


    def LookUp_inventory(self):
        item_id = input("Enter item ID to look up: ")
        if item_id in self.inventory:
            print("\nItem Details: ")
            print("ID\tName\t\tCategory\tPrice\tQuantity")
            details = self.inventory[item_id]
            print(f"{item_id}\t{details[0]}\t\t{details[1]}\t\t${details[2]:.2f}\t{details[3]}")
        else:
            print(f"Item {item_id} not found in inventory.")
            
            #^^^ function that allows you to look up the id of an Item

    def addItem(self):
        while True:
            itemID = input("Enter item ID for the new item: ")
            if itemID in self.inventory:
                print(f"Item ID {itemID} already exists. Please choose a different ID.")
            else:
                item_name = input("Enter item name: ")
                category = input("Enter category (Fruits/Dairy/Vegetable): ")
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
                new_item = [item_name, category, price, quantity]
                self.inventory[itemID] = new_item
                print(f"Item {itemID} was added to inventory.")
                break
            #^^^
            #if you pick adding a new item and the while loop is true and given the specifics,
            #the item will be created. It will break because this function should only be preformed once.

    def changeItem(self):
        itemID = input("Enter item ID to update information: ")
        if itemID in self.inventory:
            print("\nCurrent Item Details:")
            self.ItemDetails(itemID)

            item_name = input("Enter new item name: ")
            category = input("Enter new category (Fruit/Dairy/Vegetable): ")
            price = float(input("Enter new price: "))
            quantity = int(input("Enter new quantity: "))

            self.inventory[itemID] = [item_name, category, price, quantity]
            print(f"Item {itemID} information was updated.")
            print("\nUpdated Item Details:")
            self.ItemDetails(itemID)
        else:
            print(f"Item {itemID} was not found in inventory.")
            
            #^^^ Function that lets you interact and change item

    def deleteItem(self):
        itemID = input("Enter item ID to delete: ")
        if itemID in self.inventory:
            print("\nDeleted Item Details:")
            self.ItemDetails(itemID)
            del self.inventory[itemID]
            print(f"Item {itemID} was deleted from inventory.")
        else:
            print(f"Item {itemID} was not found in inventory.")
            #^^^ 
            #function that allows you to delete an item

    def findCategory(self):
        category = input("Enter category to find items: ")
        category_items = [itemID for itemID, details in self.inventory.items() if details[1] == category]
        
        if category_items:
            print(f"\nItems in Category {category}:")
            for itemID in category_items:
                print(f"{self.inventory[itemID][0]}")
        else:
            print(f"Invalid category: {category}")
            #function that allows you to find an item based on its category.. Fruit, dairy, or vegetable

    def ItemDetails(self, itemID):
        details = self.inventory[itemID]
        print("ID\tName\t\tCategory\tPrice\tQuantity")
        print(f"{itemID}\t{details[0]}\t\t{details[1]}\t\t${details[2]:.2f}\t{details[3]}")
        #function that gives you the specifics of every items details that you ask for

    def quitProgram(self):
        print("\nExiting Inventory Management System...")
        print("Thank you for using my inventory management system developed by Ryan Fanick (ID:991722325)")
        #^^^ is the final function which if you enter 7, you are given the goodbye.

#function for the menu, this function allows our menu to be interactable.
    def run(self):
        while True:
            self.displayMenu()
            choice = input("Enter your choice (1-7): ")

            if choice == '1':
                self.displayInventory()
            elif choice == '2':
                self.LookUp_inventory()
            elif choice == '3':
                self.addItem()
            elif choice == '4':
                self.changeItem()
            elif choice == '5':
                self.deleteItem()
            elif choice == '6':
                self.findCategory()
            elif choice == '7':
                self.quitProgram()
                break
            else:
                print("Invalid option. Enter a number between 1 and 7.")
                #if you dont enter numbers 1-7, you will get invalid option.

inventory_system = InventoryManagementSystem()
inventory_system.run()
#runs the whole system
