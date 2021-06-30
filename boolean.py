
print("Insert three numbers to see if they are equal.")



#1. Take 3 inputs from the user and check:
        #a. if all are equal 
        #b. any of two are equal ( use and or )



f = int(input("insert first numbers : " ))
d = int(input("insert second number : " ))
s = int(input("insert third number : " ))

if f == d == s:
	print(True)

elif f == s or f == d or d == s:
	if f == s:
		print("f is equal to s")

	elif d == s:
		print("d is equal to s")

	else:
		print("f is equal to d")


	


else:
	print(False)