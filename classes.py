
#Write a Python program to create a class and print your name as 
# a variable in the class and print your age using a function in the class

class PersonInfo:
  personName = "Asante"

  def age(self):
    return 9 

people = PersonInfo()
print(people.personName)
print(people.age())

class A:
  def __init__(self,b):
    self.b=b
  def display(self):
    print(self.b)
obj=A("Hello")
del obj