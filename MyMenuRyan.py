

import math
#importing math so we can do the math for our functions

def draw_triangle():
    height = int(input("Enter the height of the triangle: "))
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))
        #math for the draw_triangle function

def draw_rectangle():
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    for i in range(height):
        print("*" * width)
        #math for the draw_rectangle function

def find_polygon():
    sides = int(input("Enter the number of sides of the polygon: "))
    if sides < 3:
        print("A polygon must have at least 3 sides.")
    else:
        angles = (sides - 2) * 180
        print(f"The sum of angles in a {sides}-sided polygon is {angles} degrees")
        #math for the find_polygon_angles function

def facto_power():
    n = int(input("Enter a number (n) for the Facto-Power Series: "))
    result = 1
    for i in range(1, n + 1):
        result *= i**i
    print(f"The Facto-Power Series result for {n} is {result}")
    #math for the factor_power functions

def check_password():
    password = input("Enter a password: ")
    special_chars = '0123456789!@#$%^&*()_+[]{};:\'".,?/\\~`-' #special characters for password

    #password length is 6-20 characters long
    if len(password) < 6 or len(password) > 20: #length of password has to be min 6 and max is 20 characters
        print("Password length must be between 6 and 20 characters.")
        return

    #must contain one uppercase 
    if not any(char.isupper() for char in password):
        print("Password must contain one uppercase character.")
        return

    #password must contain lower case
    if not any(char.islower() for char in password):
        print("Password must contain one lowercase character.")
        return
    if not any(char in special_chars for char in password): #allows these special characters into the password
        print("Password must contain one digit or special character (invalid if '>' or '<').") #does not allow chars <>
    else:
        print("Valid password")
        #else valid if user gives all the requirements above


def main(): #this is the main function, the menu, which is the most important
    while True: #made it a while loop so the menu keeps continue until you quit it
        print("My menu Options:")
        print("1. Draw Shape")
        print("a) Triangle")
        print("b) Rectangle")
        print("2. Find Polygon Angles")
        print("3. Facto-Power Series")
        print("4. Check Password")
        print("5. Quit")
        
        #^^ these are all the options
        
        choice = input("Enter your choice: ")

        if choice == "1":
            shape_choice = input("Choose a shape (a for Triangle, b for Rectangle): ")
            if shape_choice == "a":
                draw_triangle()
                break #putting break at the end of each function so the menu doesnt constantly show up
            elif shape_choice == "b":
                draw_rectangle()
                break
            else:
                print("Invalid choice for shape.")
                break
        elif choice == "2":
            find_polygon()
            break
        elif choice == "3":
            facto_power()
            break
        elif choice == "4":
            check_password()
            break
        elif choice == "5":
            print("Thank you for using my menu program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.") #if user does not
            #input a valid choice thats not 1-5 'invalid choice' will show up
            break

if __name__ == "__main__":
    main()
