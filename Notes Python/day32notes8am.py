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
    def __init__ (self,n="",g=1):# name and grade get their values from the parameter list
                           # but coworkers and students are initialized to []
        self.coworkers = []  # a list of other Teachers
        self.students = []
        self.name = n
        self.grade = g

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

class Student:
    def __init__(self,n="",gp=0.0):
        self.name = n
        self.gpa = gp
        self.teachers = []
    def __str__(self):
        return self.name
    def __eq__(self,other):
        if self.name == other.name and self.gpa == other.gpa:
            return True
        else:
            return False
        
    
joey = Student("Joseph Brown",3.0)
burns = Teacher("Mr. Burns",10)
joe = Student("Joseph Brown",3.0)
burnsy = Teacher ("Mr. Burns", 10)
# you as the programmer decide whether two objects are the same
print(joey == joe)  # calls the __eq__ method if there is one
print(burnsy == burns)   

joey.teachers.append(burns)
burns.students.append(joey)



print(burns.students[0].gpa)
print(joey.teachers[0].grade)

joey.gpa += .1


print(burns.students[0].gpa)
print(joey.teachers[0].grade)

burns.move_up()
print(burns.students[0].gpa)
print(joey.teachers[0].grade)





        
    
    























### test your code this way...
##
##frizzle = Teacher("Ms Frizzle",4)
##print(frizzle)
##frizzle.move_up()
##print(frizzle)
##
##frizzle.get_coworker(Teacher("Mr. Burns",11))
##
##print(frizzle)
##
### how could you print out the list of the coworkers?
##frizzle.show_coworkers()

























    
