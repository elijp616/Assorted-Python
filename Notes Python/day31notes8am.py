# day 31
from day30notes9am import Pet


# object oriented programming is a way of organizing data and methods into
# named sections called classes - individual instances of a particular class are
# called objects of that class


class PetStore:
    def __init__ (self,n):  # assigns values to your attributes
        self.name = n
        self.petlist = []
        
    def __str__(self):       # returns a string representation of the object
        return self.name + "!"
    
    def add_pet(self,p):
        self.petlist.append(p)


##store1 = PetStore("Pet World")
##store2 = PetStore("Little Critters")
##print(len(store2.petlist))
##
##print(store1)
##
##lily = Pet("Lily","dog")
##
##store1.add_pet(lily)
##
##spink = Pet("Spink","rabbit")
##
##store1.add_pet(spink)
##
##print(len(store1.petlist))




# OOP Coding 1

class Teacher:
    def __init__ (self,n,g):
        self.name = n
        self.grade = g
        self.coworkers = []  # a list of other Teachers

    def __str__(self):
        return self.name + " has " + str(len(self.coworkers)) + " coworkers."

    def move_up(self):
        if self.grade in [1,2,3]:
            self.grade += 1
        elif self.grade in range(4,13):
            self.grade += 2
        else:
            pass
        
    def get_coworker(self,t):
        self.coworkers.append(t)

    def show_coworkers(self):
        for item in self.coworkers:
            print(item.name)

# test your code this way...

frizzle = Teacher("Ms Frizzle",4)
print(frizzle)
frizzle.move_up()
print(frizzle)

frizzle.get_coworker(Teacher("Mr. Burns",11))

print(frizzle)

# how could you print out the list of the coworkers?
frizzle.show_coworkers()

























    
