"""Programmer :VYCE_TECH
Program :an application that gives current date,month and time,
         and explains  information about python  functions like
         the print function and input function to non-python
         programmers.

"""

print("Hi! user,Welcome to the VYCE python program")
print("Please input your name and press enter to begin")
name = input("What is your name:")

"""
after user enters the name, the program will give the current date
"""
print("***Hello user,Do you know what time it is?***")
print("This is your current year,month and date")


from datetime import datetime
now = datetime.now()
current_year = now.year
current_month = now.month
current_time = now.day

print(now.year)
print("is the Year")
print("**************************************************************************************************")
print(now.month)
print("is the Month")
print("**************************************************************************************************")
print(now.day)
print("is the Date")
print("**************************************************************************************************")

print("This is current time in Hot date view.")
from datetime import datetime
time = datetime.now()
print(time)

print("Are you ready to learn more about python functions?:YES/NO")
print("<<Make sure your response is in BLOCK letters>>")
name = input()

if name == 'NO':
    print("Goodbye user!!!")
    quit()


print("PYTHON FUNCTIONS INCLUDE:")
print("> 1.print")
print("> 2.input")


name = input("Press Enter to proceed to select the first function :")

name = input("Enter the keyword print")
help(print)

name = input("press Enter to proceed to the second function")
name = input("Enter the keyword input")
help(input)



print("To learn more about python programming please visit www.python.org")
print("***Thank you for using the VYCE_app***")
print("{GOODBYE}")
quit()







