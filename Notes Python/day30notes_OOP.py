# day 30 - Object Oriented Programming
#
# code is divided into user defined data types called classes

# you have been using classes already: the string class and the list class

# classes provide methods that are called with the . operator
# classes also have attributes 

myname = "Melinda"   # creates an object of the String class
print(myname.lower()) # the string class provides this method for its objects
print(type(myname))


class Pet:

    def __init__ (self, aname, akind):
        self.name = aname   # the Pet class has 3 attributes  name, kind and age
        self.kind = akind
        self.age = 1


    def speak(self):   # self gets its value from the thing in front of the .
        if self.kind == "cat":
           print(self.name + " says meow!")
        else:
            print(self.name + " says woof!")

    def get_older(self):
        self.age += 1

    def __str__(self): # returns a string that is printed out when you try to print
                         # an object of this class
        return "A " + self.kind + " named " + self.name + " that is " + str(self.age) + "."                    
        

pet1 = Pet("Beauty","cat")
pet2 = Pet("Lily","dog")

for num in range(6):
   pet2.get_older()

print(pet1.age)
print(pet2.age)



print(pet1) # calls the __str__ method passing it pet1 as the parameter
print(pet2)

pet1.speak()
pet2.speak()
