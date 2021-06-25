#author : Asante
#calculator program
#date 19/06/2021


print("Welcome to Asante's personal calculator.")
number1 = int (input("Please pick the first number you want to calculate:"))
print(number1)


operation = int (input(" Choose 1 to add, 2 to subtract, 3 to multiply, 4 to divide:"))
print(operation)


number2 = int (input("Please pick a second number to multiply, divide, subtract, or add by:"))

def multiply(x , y):
	return x * y

def divide(a , b):
	return a / b

def add(s , l):
	return s + l

def subract(h , p):
	return h - p

total = 0


if operation == 1:
	total = add(number1, number2)   
	print (total)
elif operation == 2:
	total = subract(number1, number2)
	print (total)

elif operation == 3:
	total = multiply(number1, number2)
	print (total)

elif operation == 4:
	total = divide(number1, number2)
	print (total)                                   

else:
	print("Invalid input.")

