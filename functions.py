#Functions/Methods - A block of code used to perform a task


# 1. Standard - Library Functions/Inbuilt Functions - Already exists

y = max(56,67,345,999,28,765,976,85)
print(y)

x = min(13,12,9,82,73,91,67)
print(x)

# 2. User-Defined Functions

def school():
    print("eMobilis")

school() #Calling a function


#Parameters/Variables
#Arguements/Values
def multiply(x, y):
    print(x * y)

multiply(34, 10)


def student(name, age, gender):
    print(name, age, gender)

student("Clement",18,"Male")
student("Lewis", 18,"Male")
student("Christian",19,"Male")

#Python program to display details of 5 employees at eMobilis
#Use a user defined function with the help of parameters and arguments
#Details - Fullname, Position, age, gender

print()
print()


#Assignment
def employee(fullname,position,age,gender):
    print(fullname,position,age,gender)

employee("Okoth Owino", "Dean of Studies", 37, "Male")
employee("Kirk Munene", "Receptionist", 29, "Male")
employee("Priscah Mulei", "Finance Manager", 40, "Female")
employee("Larry Mwirigi", "Lecturer", 31, "Male")
employee("Florence Wesonga", "Lecturer", 30, "Female")
