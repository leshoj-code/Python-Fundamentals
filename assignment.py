# Program to check if a number is even or odd

number = int(input("Enter a number: "))

if number  == 0:
    print("Neutral number")

elif number % 2 == 0:
    print("The number is even.")

else:
    print("The number is odd.")
