# Day 15 modules

##import math   # math.sqrt()          - my preferred way for readability
##from math import *   # sqrt()
##import math as m  # m.sqrt()   
##
##
##import string            string.punctuation   gives me "<>()$..."                 
##from string import *     punctuation              "<>()$...."
##import string as s        s.punctuation


import random as r

print(r.randrange(1,6))  # gives a random integer between 1 and 5 inclusive
print(r.random())   # gives a random float between .000000 and .99999999
##
### guess the die roll
##num = r.randrange(1,7)
##guess = int(input("Guess the die roll: "))
##while num != guess:
##    print("Wrong!")
##    guess = int(input("Guess the die roll: "))
##print("Awesome!")


girls = ["Julia","Madelyn","Jessica"]
boys = ["Jay","Jeremy","Ed","Eric","Ben"]

if len(girls) <= len(boys):
    stop = len(girls)
else:
    stop = len(boys)
    
for num in range(stop):
    girlnum = r.randrange(len(girls))
    boynum = r.randrange(len(boys))
    print("{} likes {}.".format(boys[boynum],girls[girlnum]))


# what if the same name keeps getting picked?
    del girls[girlnum]
    del boys[boynum]

# make your own module....
# any .py file can be imported - must be in the same folder
from modulestuff import * # don't put .py
func1()
func2()

# write a function called encode that takes a name and encodes it
# randomly picks a place in the name to start then wrap around



def encode(name):
    name = name.lower()
    place = r.randrange(len(name))
    firstpart = name[place:]
    secondpart = name[:place]
    return firstpart + secondpart

print(encode("Jessica"))
    











