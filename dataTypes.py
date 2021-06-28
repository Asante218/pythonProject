#Authuor: Asante
#date : 25/06/2021

def add(s , l):
	return s + l



#strings 
name = "Asante"
lastName = "Mwesigwa"




# integer
age = 9
yearBorn = 2011


# float
decimal = 1.5

decimal = add(decimal, 10)

print("My name is " , name ,",I am " , age , "years old and I was born in" , yearBorn , "I can,t wait til i am " , decimal  , "years old .")





#list
numberList = [ 1 , 2 , 3 , 4 , 5]

decimaList = [ 0.5 , 1.5 , 2.5 , 3.5 , 4.5 , 5.5]

stringList = ["happy" , "sad" , " angry " ]

mixedList = [ 1 , 1.5 , "happy"]


for x in mixedList:
    print( x , end= ' ')

#, end = '')

# dictionary

thisdict = {
	"good":"bad",
	"heroic":"evil"
}
print(thisdict)

person = {
	"name":"Asante",
	"eyeColor":"brown",
	"hairColor":"black",
	"age":9,
	"height":14,
	"weight":30
}


all_pairs = list(person.items())
print('First Key value pair: ', all_pairs[0])

print(person.get('name'))
print(person['name'])
#My name is Asante, I am 9 years old and I wans born in 2011