#author : Asante
#calculator program
#date 19/06/2021


print("Welcome to Asante's personal calculator.")
number1 = int (input("Please pick the first number you want to calculate."))
print(number1)


operation = int (input(" Choose 1 to add, 2 to subtract, 3 to multiply, 4 to divide."))
print(operation)


number2 = int (input("Please pick a second number to multiply, divide, subtract, or add."))



total = 0


if operation == 1:
	total = number1 + number2
	print (total)

elif operation == 2:
	total = number1 - number2
	print (total)

elif operation == 3:
	total = number1 * number2
	print (total)

elif operation == 4:
	total = number1 / number2
	print (total)

else:
	print("Invalid input.")



