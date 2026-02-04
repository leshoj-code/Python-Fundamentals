age = 21 #integer
length = 45.6 #Float
greeting = "Hello there" #String
hasFeathers = True #Boolean

#Data Structures - Multiple values stored
#one variable.
fruits = ["Banana", "Mango", "Papaya"] # List - Ordered and changeable - Different datatypes
courses = ["MIT", "Data Science", "Cybersecurity"] #Array - Similar datatypes
cars = ("Mercedes", "Toyota", "Volkswagen", "Nissan") #Tuple - ordered and unchangeable
countries = {"Zambia", "Canada", "India", "Kenya"} #Set - Unordered and unchangeable
Student = {
    "firstname" : "Esther",
    "course" : "MIT",
    "age" : 19,
    "nationality" : "Kenyan",
    "gender" : "Female"
} #Dictionary - Key value pair



print(age)
print("The length is", length)
print(fruits)
print(countries)
print(Student)
print(Student["nationality"])


#Typecasting - converting one data type to another.
print(float(age))
print(int(length))
