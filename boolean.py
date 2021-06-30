first = "hello world"





#boolean exercise

print("i am a computer")

#Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2. If it is, show the message "Math is fun."`

if 1 < 2 and 4 > 2:
	print("math is fun ")

nope = ""

name = input("enter your name : ")

print("hello, " + name )



#Ask the user for a number. If the number is negative, show a message that says "That number is less than 0!" If the number is positive, show a message that says "That number is greater than 0!" Otherwise, show a message that says "You picked 0!.


number = int(input("enter a number :"))

if number > 0:
	print("That number is greater than" , 0 , "!")

elif number == 0:
	print("You picked " , 0 , "!.")

else:
	print("That number is less than " , 0 ,  "!")


print("see if the numbers are eqaul")

x = int(input("insert number one: " ))
y = int(input("insert number two: " ))

if x == y:
	print(True)
else:
	print(False)


print("Insert three numbers to see if they are equal.")



#1. Take 3 inputs from the user and check:
        #a. if all are equal 
        #b. any of two are equal ( use and or )



f = int(input("insert first numbers : " ))
d = int(input("insert second number : " ))
s = int(input("insert third number : " ))

if f == d == s:
	print(True)

elif f == s:
	print("f and s are equal")


elif f == d:
	print("f and d are equal")


elif d == s:
	print("d and s are equal")


else:
	print(False)