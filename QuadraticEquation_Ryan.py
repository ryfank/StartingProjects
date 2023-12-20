
#input 
import math #importing math for math.pow

name = (input("Please enter your name: "))
studentNumber = (input("Enter your Sheridan Student Number: "))

a = float(input("Enter a: ")) 
b = float(input("Enter b: "))
c = float(input("Enter c: "))
#first part is just inputting your name, your student number and what you want.

#----------------------------------------------------------
#process

discriminant = b**2 - 4*a*c #the formula given
if discriminant >= 0: #this is for if there is two real roots
        root1 = (-b + math.pow(discriminant)) / (2*a) #the equation given
        root2 = (-b - math.pow(discriminant)) / (2*a)
elif discriminant == 0: #else if the discrim is equalled to 0 then it will give you the other formula
        root1 = -b / (2*a) #this is if there is one real root
else:
        print(f"There are no real roots of the equation.") #if there is no roots then it will give you this output
        
#----------------------------------------------------
#output

print(f"Discriminant: {discriminant:.2f}") #.2f is a float 
#this will show you the discriminant of your answer

print(f"Quadratic equation solved by:{name}, {studentNumber}")


