#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW06 - TRY/EXCEPT & DICTIONARIES
"""
__author__ = """ Elijah Peterson """
__collab__ = """ I worked on this assignment with Chris Eckart using only this semester's notes"""

"""
Function name: make_gamertag
Parameters: list, str
Returns: str 
Description: Write a function that takes in a string and a list of integers
and adds indices (specified in the list) from the string into your
soon-to-be tag. Anytime the desired index does not exist, add in a “0” zero
to the gamertag, but if the index is valid, add the corresponding character
as well as another “x” just for spice. When you have gone through all entries
of the list, surround the tag with square “[“  “]” brackets and return the string.

"""
def make_gamertag(start,index):
    newstring = ""
    for i in index:
        try:
            newstring += start[i] + "x"
        except:
            newstring += "0"

    newstring = "[" + newstring + "]"
    return newstring


"""
Function name: split_the_loot
Parameters: dict, list, int/float, int
Returns: float
Description: Write a function split_the_loot that takes in these four things
and also the number of thieves to split between. If the letter case of the
items in the list differ from the dictionary entries at all,
do not count it to the total. (i.e. “hello” != “hEllo”)

If any of the parameter types are invalid, the code should catch it and
return a string saying “TypeError”. If any of the catalog prices are negative
and it is in the items list, return “Negative”. If the number of burglars is 0
or less, return “BurglarError”
"""
def split_the_loot(store,stolen,cash,burg):
    total = 0
    try:
        for i in store:
            for x in stolen:
                if i == x and store[i]<0:
                    return "Negative"
                elif i==x:
                    total += store[x]
    except TypeError:
        return("TypeError")

    if burg > 0:
        
        money = total + cash
        split = round(money/burg,2)
        return split
    elif burg <= 0:
        return "BurglarErorr"





"""
Function name: football_stars
Parameters: dict, dict
Returns: dict 
Description: Write a function that takes in two different dictionaries, one with
a state name as the key and a list of teams in that state as the value. The other
dictionary has an NFL team name as the key and the name of a top player on that
team as the value. If a player in the latter dictionary is on a team that appears
in the first list, add the player’s name as a key in a new dictionary and match it
to a tuple of the state and the team name that the player is on.

"""
def football_stars(teams,players):
    newdict = {}
    for i in teams:
        for x in players:
            if x in teams[i]:
               newdict[players[x]] = (i,x)
    return newdict

    

"""
Function name: pair_rivals
Parameters: dict, dict
Returns: dict
Description: In this function you will take in two dictionary arguments, and return
a new dictionary. Both parameters will have one string keys paired to one string
values. Each key will represent a certain character and the value will be the rival
of that character. If one character’s rival in the first dictionary is that rival’s
rival in any of the dictionaries, add a tuple of both names as a key (first, second)
in a new dictionary, paired to True as its value. In other words, only add it into
the new dictionary if “character”:”rival” in one is found as “rival”:”character” somewhere.
"""
def pair_rivals(one,two):
    newdict = {}
    newtup = ()
    for a in one:
        for b in one:
            if a == one[b]:
                newtup += a,
    
    for x in one:
        for i in two:
            if x == two[i] and x not in newtup:
                newtup += x,
            if  one[x] == i and i not in newtup:
                newtup += one[x],
    for c in two:
        for d in two:
            if c == two[d] and c not in newtup:
                newtup += c,
    if newtup != ():
        newdict[newtup] = True
        return newdict
    else:
        return newdict
list1 = {"Kanye West": "Taylor Swift", "Messi": "Ronaldo"}
list2 = {"Taylor Swift": "Ex-Boyfriends"}
test7 = pair_rivals(list1,list2)
print(test7)

"""
Function name: zoo_keeper
Parameters: list
Returns: dict
Description: Write a function called zoo_keeper that takes in a list of tuples
with the animal’s type, the animal’s species and the number of each animal.
You should return a dictionary with the animal’s type as a key and a dictionary
with the species and the number of each animal as its value. If an animal’s type
or species appears more than once, you should add the population to the existing
animal. All tuples will be completely lower cased.

"""
def zoo_keeper(animals):
    newDict = {}
    for i in animals:
        newdict2 = {}
        tp,spec,num = i
        if spec in newdict2:
            newdict2[spec] = newdict2[spec] + num
        else:
            newdict2[spec] = num

        if tp in newDict:
            if spec in newDict[tp]:
                newDict[tp][spec] += num
            else:
                newDict[tp][spec] = num
        else:
            newDict[tp] = newdict2

    return newDict


"""
Function name: animal_locator
Parameters: dict
Returns: dict
Description: Write a function called animal_locator that takes in a dictionary
containing zoo locations as keys and their values being a list of tuples with the
specific animal and the population of that specific animal at that zoo. You should
return a dictionary containing the animals as keys and their values being a tuple
with their first element being an ordered list of all the zoo locations based on
how many animals are at each location (greatest to least) and the second element
being an integer of the total population of that specific animal.
You do not have to take in account case sensitivity. 

"""
def animal_locator(dict1):
    animalp = {}
    for zoo in dict1:
        for animalTup in dict1[zoo]:                  
            if animalTup[0] in animalp:
                animalp[animalTup[0]] = (animalp[animalTup[0]] + animalTup[1])
            else:
                animalp[animalTup[0]] = animalTup[1]
    for i in animalp:
        location = []
        location2 = []
        cityList = []
        for zoo in dict1:
            for animalTup in dict1[zoo]:
                if i == animalTup[0]:
                    if zoo not in cityList:
                        cityList.append(zoo)
                        location2.append((animalTup[1],zoo))           
        location2.sort(reverse = True)
        similar = []
        for locations in location2:
            for location3 in location2:
                if (locations[0] == location3[0]) and (locations != location3):
                    similar.append(locations[1])
                    similar.append(location3[1])
                    similar.sort(reverse = True)         
            location.append(locations[1])
        animalp[i] = (location,animalp[i])
    return animalp
