
#input
    
num = int(input("Enter an integer between 10 and 100: ")) #enter number

studentNumber = (input("Enter your Sheridan Student Number: ")) #enter your sheridan ID

Name = (input("Please enter your name: ")) #your name

#-----------------------------------

#process

endNumber = int(studentNumber[-1]) #your student number, if not -1 then it will make all of your output invalid

if endNumber == 0 and endNumber == 1:  #if the end number is = to 0 or end number is = to 1
        divisor = 10 #the divisor is 10 given
else:
        divisor = endNumber #else the divisor is equalled to the end digit

if num % divisor == 0: #if the num you inputted is divisible by 10 (or end number) it equals 0
        print(f"Input {num} is divisible by the last digit of my student number ({studentNumber}) or by 10. Goodbye!")
else:
        print(f"Input {num} is NOT divisible by the last digit of my student number ({studentNumber}) or by 10. Goodbye!")

#---------------------------  

#output

print(f"{Name}, {studentNumber}") #the student number and name you gave

print(f"The input number: {num}") #the number you gave 

 #the output you recieve, letting you know whether or not your output is divisible by that number


