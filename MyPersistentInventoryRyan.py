
import os #importing os module, interacting with the os

def load_inventory(Inventory_Ryan): #creating inventory
    inventory = []
    if os.path.exists(Inventory_Ryan): 
        with open(Inventory_Ryan, 'r') as file:
            for line in file:
                item_data = line.strip().split()
                inventory.append(item_data)
    return inventory 

def saveInventory(Inventory_Ryan, inventory): #this function is if you want to save what
    with open(Inventory_Ryan, 'w') as file: #you have in inventory
        for item in inventory:
            file.write(' '.join(item) + '\n') #tuple then next line

def showItems(inventory): #showing all items in iventory
    for item in inventory:
        print(' '.join(item)) #join creates a tuple of items

def lookUpItem(inventory, item_id): #looking up item in inventory including its ID
    for item in inventory:
        if item[0] == item_id: #first element being iterated to equal item_id 
            return item
    return None #return none means theres nothing present in the inventory

def addItem(inventory): #this is a function being added in the inventory us the ID  
    item_id = input("Enter item id: ")
    # checking if the item id already exists
    if lookUpItem(inventory, item_id):
        print("Item id already exists. Please enter a different item id.")
        return

    itemName = input("Enter item name: ") #Adding new item inventory name
    itemCategory = input("Enter item category: ") #Adding item category
    itemPrice = input("Enter item unit price: ") #Adding item price
    itemQuantity = input("Enter item quantity: ") #Adding how much of the items quantity

    new_item = [item_id, itemName, itemCategory, itemPrice, itemQuantity] 
    
    #characteristics of the new item
    inventory.append(new_item)
    print("Item added successfully.")

def changeItem(inventory, item_id):
    #changing the item inventory
    index = -1 #keeps track of index in inventory
    for i, item in enumerate(inventory):
        if item[0] == item_id:
            index = i
            break

    if index == -1:
        print("Item not found.")
        return
    #will print 'item not found' if you do not put in a valid itemID from the inventory


    #updating information from user
    itemName = input("Enter new item name: ")
    itemCategory = input("Enter new item category: ")
    itemPrice = input("Enter new item unit price: ")
    itemQuantity = input("Enter new item quantity: ")

    #update the item 
    inventory[index] = [item_id, itemName, itemCategory, itemPrice, itemQuantity]
    #all the characteristics of the item
    print("Item updated successfully.")

#deleting item from inventory
def deleteItem(inventory, item_id):
    for i, item in enumerate(inventory):
        if item[0] == item_id:
            del inventory[i] #deletes the item
            print("Item deleted successfully.")
            return
    print("Item not found.")
    #if itek id is not entered correctly 'item not found' will show

#finding items by category
def findCategory(inventory, category):
    items_in_category = [item[1] for item in inventory if item[2] == category]
    return items_in_category

def main(): #my main menu function to make everything work, including the txt file and the inventory
    file_name = 'Inventory_Ryan.txt' #the txt file the items are stored in
    inventory = load_inventory(file_name) #puts the inventory into the txt file

    while True:
        print("\nInventory Options:")
        print("1. Show all items")
        print("2. Look up the inventory")
        print("3. Add an item to the inventory")
        print("4. Change an item")
        print("5. Delete an item")
        print("6. Find items given category")
        print("7. Quit the program")

        option = input("Enter your choice (1-7): ")

        if option == '1':
            showItems(inventory)
            break
        elif option == '2':
            item_id = input("Enter item id: ")
            item = lookUpItem(inventory, item_id)
            if item:
                print("Item found:")
                print(' '.join(item))
                break
            else:
                print("Item not found.")
                break
        elif option == '3':
            addItem(inventory)
            saveInventory(file_name, inventory)
            break
        elif option == '4':
            item_id = input("Enter item id to change: ")
            changeItem(inventory, item_id)
            saveInventory(file_name, inventory)
            break
        elif option == '5':
            item_id = input("Enter item id to delete: ")
            deleteItem(inventory, item_id)
            saveInventory(file_name, inventory)
            break
        elif option == '6':
            category = input("Enter category to find items: ")
            items_in_category = findCategory(inventory, category)
            if items_in_category:
                print(f"Items in category {category}: {', '.join(items_in_category)}") #joins the two together
                with open(f'Inventory_Ryan.txt', 'w') as cat_file: 
                    cat_file.write(f"Ryan Fanick, 991722325 #\n")
                    cat_file.write(f"Category: {category}\n")
                    cat_file.write(f"Items: {', '.join(items_in_category)}\n")
            else:
                print("Invalid category or no items found in the category.")
                break
        elif option == '7':
            print(f"Thank you for using my program. Goodbye! Developed by Ryan Fanick (991722325)")  # Replace with your actual full name and student number
            break
        else:
            print("Invalid option. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()

