

#input

print("Basal Metabolic Rate (BMR) Calculator") #establishing what BMR calculator 
sex = input("Enter your sex (Male/Female): ") 
age = int(input("Enter your age (in years): ")) 
weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in cm): "))

Name = (input("Please enter your name: "))
studentNumber = (input("Please enter your student number: "))

#Inputting the stats so we can calculate everything later

#-----------------------------------------------------

#process

if sex == "male" or "m": #if you input male or m it will calculate
       bmr = 66.5 + (13.75 * weight) + (5.003 * height) - (6.755 * age) #formula given
       print(f"Your Basal Metabolic Rate (BMR) is: {bmr:.2f} calories per day - Male") #for male 
       
if sex == "female" or "f": #if you input female or f it will calculate
       bmr = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age) #formula given
       print(f"Your Basal Metabolic Rate (BMR) is: {bmr:.2f} calories per day - Female") #for female
else:
        print("invalid sex input")
#-----------------------------------------------------------
#output

print(f"BMR calculator by: {Name}, {studentNumber}")
