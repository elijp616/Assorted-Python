# Day 18 - advanced tuples

# start with the solution from last time's mini-quiz, then add on to it

# Write a function called swap_names that takes in a list of tuples containing someone's last name and first name.  Return a list of tuples containing each person's first name and their last name with a unique number at the end of the last name.
def swap_names(tuplist):
    newlist = []
    count = 0
    for tup in tuplist:
        newtup = (tup[1],tup[0] + str(count))
        newlist.append(newtup)
        count += 1               
    return newlist    
 
tupList = [("Johnson", "Jakob"), ("Henry", "Damian"), ("Yang", "Caitlin"), ("Yap", "Jasmine")]

result = swap_names(tupList)

print(result)





# tuples are really useful for swapping values

a = 4
b = 3
(a,b) = (b,a)
print(a)
print(b)





mytup = ('physics','10am','2300',3)
#mytup[0] = 'chemistry'      # runtime error!
courses = [('physics',4),('chemistry',3)]

tup1 = ()   # an empty tuple
tup2 = (3,5)  # length is 2
tup3 = ('cat',)  # comma is necessary if there is only one item
tup4 = ('dog')

print(type(tup1))


# tuples can be contatenated or multiplied
num = 999
tup5 = (3,4) + (4,5)
tup5 += (num,)
print(tup5)

# one advantage of tuples is that you can return a tuple from a function so that
# your function returns more than one thing

import math
def circle_stuff(radius):  # returns the area and the circumference of a circle
    return (math.pi * radius ** 2, 2 * math.pi * radius)


# try this... write a function that takes as a parameter a list of names and ages and returns
# the name of the oldest student

tuplist = [('joe',23),('mary',24),('elena',20),('melinda',29)]

def get_oldest(tuplist):
    highest_age = -1
    highest_name = ""
    for tup in tuplist:
        if tup[1] > highest_age:
            highest_age = tup[1]
            highest_name = tup[0]
    return highest_name

print(get_oldest(tuplist))

            
# multiplying tuples
tup1 = (3,4)
print(tup1 * 2)
print((3) * 2)


# nested lists and tuples
bigtuple = ([1,2,3],[2,2,2],'A',(1,1))
print(bigtuple[0][2])
biglist =  [[1,2,3],[2,2,2],'A',(1,1)]
print(biglist[0][2])

# mutable vs.immutable
biglist[0][2] = 999
print(biglist)



# what are tuples good for?
# packing related data to use as a key into a dictionary for looking stuff up

# tuples only have two methods .count and .index
# tuples have several functions, but the only one you need to know is len


grades = [("Jordan",88,99,100),("Mary",99,100,66),("Trent",77,88,99)]
# who made the highest grade on test 3?
# how many students improved between test1 and test2?


# practice tracing tuples
count = 3
for tup in grades:
    if tup[0][2] == "r":
        count -= 1
print(count)        
    
##
##tot = 0
##for tup in grades:
##    if tup[1]>95:
##        tup[2] -=5   # error
##print(grades)

#Mini quiz
for place in range(len(grades)):
    tup = grades[place]
    newstring = ""
    for i in range(len(tup[0])):
        newstring = tup[0][i] + newstring
        print(newstring)
    grades[place] = (newstring,) + tup[1:]
print(grades[0][0][0])


        
        
    





    




















