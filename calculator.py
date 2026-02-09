x = float(input("Enter first number:"))
print(x)

op = input("Enter an operator (+,-,*,/):")
print(op)

y = float(input("Enter second number:"))
print(y)

if op == "+":
    answer = x + y

elif op == "-":
    answer = x - y

elif op == "*":
    answer = x * y

elif op == "/":
    if y == 0:
        answer = "Error: Division by zero"
    else: answer = x / y

else: answer = "Error: You have entered a wrong operator"

print("The answer is:", answer)
