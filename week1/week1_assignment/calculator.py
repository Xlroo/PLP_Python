"""
Instructions:

Basic Calculator Program

Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.
"""
#Ask for input numbers 
num1 = float(input("Kindly input first number "))
num2 = float(input("Kindly input second number "))
operation = input("Choose a mathematical operation(+, -,/,**) ")


#Calculate operation
#result = num1 operation num2
if operation == "+":
	result = num1 + num2 
elif operation == "-":
	result = num1 - num2 
elif operation == "/":
	result = num1/ num2 
elif operation == "*":
	result = num1 * num2
elif operation == "**":
	result = num1 ** num2
else:
	print("Invalid operand")
	exit()

print(f"Your input is {num1} {operation} {num2} = {result}")

