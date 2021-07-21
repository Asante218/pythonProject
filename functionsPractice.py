
#Write a function calculation() such that it can accept two variables 
#and calculate the addition and subtraction of them. And also it must return both 
#addition and subtraction in a single return call



number1 = int(input("insert the first number : "))


number2 = int(input("insert the second number : "))




def calculation( x , y ):
	return x + y , x - y
	
	

total = calculation( number1, number2 )

print(total)


#Write a function called lastElement. This function takes one parameter (a list)
# and returns the last value in the list. It should return None if the list is empty.


def lastElement(list):
	return list[-1]


list1 = [ 1 , 2 , 3 , 4 , 5 ]
print((lastElement(list1)))




# Wrtie a function called singleLetterCount. This function takes in two parametrs (two strings).
# The first parameter should be a word and second should be a letter. The function returns
# the number of times that letter appears in the word. The function should be case insensitive (does not
# matter if the input is lowercase or uppercase). If the letter is not found in the word, the function
# should return 0.

letter = input("insert a letter : ")
word = input("insert a word : ")

def singleLetterCount(g , good):
	if g in good:
		return "Yes!" , good.count(g)


	else:
		return "none" , 0


	

print(singleLetterCount(letter , word))

def f(a, b = 1, c = 2):
   print('a is: ',a, 'b is: ', b, 'c is: ', c)



print("this is for function f")
f(2, c = 2)
f(c = 100, a = 110)

