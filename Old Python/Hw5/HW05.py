#!/usr/bin/env python3

import rate
"""
Georgia Institute of Technology - CS1301
HW05 - Tuples and Modules
"""
__author__ = """ Elijah Peterson """
__collab__ = """ I worked with Christopher Eckart on this assignment """

"""
Function: yelp_rating
Parameters: original (float), num (float), operation (string)
Returns: A float

Description: After visiting restaurants, you want to change the rating of the place.
Provided is a Python file (rate.py) containing functions for simple calculations that
you will need to import and use for this function.This function will take in an operation
(as a string) that will either be '+', '-', '*', or '/', as well as two other parameters
that are floats. original stands for the original rating and num is the number you want
to perform the operation with. Depending on the operation that is passed in, call the appropriate
function from the provided Python file and pass in the original and num arguments as parameters
to the function. Return the result of your calculation. If the operation passed in is not one of
the four valid symbols, return None.  If you do not use the functions in rate.py to solve this function
then you will not receive credit for this function.

Note: Round to one decimal point. 

"""

def yelp_rating(orginal,num,operation):
    orginal = float(orginal)
    num = float(num)
    if operation == "+":
        new = rate.add(orginal,num)
    elif operation == "-":
        new = rate.subtract(orginal,num)
    elif operation == "*":
        new = rate.multiply(orginal,num)
    elif operation == "/":
        new = rate.divide(orginal,num)
    else:
        return None
    new = round(new,1)
    return new

"""
Function name: register_passport
Parameters: information (string)
Returns: A tuple 

Description: Before you pick your flights and travel destinations, you need to
make sure that your passport has been fully registered since the process usually
takes a long time! Write a function that takes in a string that holds information
about a person registering for their passport. You can assume that the string will
always be in the format “NAME: AGE, COUNTRYCODE”. Return a tuple in the format (COUNTRYCODE (string), NAME (string), AGE (int)).

Note: There is a space before AGE and before COUNTRYCODE. The tuple returned must
not have any spaces around the strings. For example, it should be “Caitlin Yang”, not “ Caitlin Yang  ”.


"""

def register_passport(info):
    name = ""
    age = ""
    country = ""
    namerng = info.find(":")
    for x in info[0:namerng]:
        name += x
    agerng = info.find(",")
    for i in info[namerng+1:agerng]:
        age += i
    for z in info[agerng+1:]:
        country += z
    age = age.strip()
    age = int(age)
    country = country.strip()
    b =(country,name, age)
    return(b)

"""
Function name: location_ideas 
Parameters: list of tuples
Returns: tuple 
Description: Now after you have registered your passport, you need to brainstorm what
locations you want to travel to. Write a function that takes in a list of tuples in the
form (LOCATION (string), MILES_AWAY (int)). Return a tuple of the locations in order from
closest (lowest miles away) to farthest (greatest miles away). If the list passed in is empty,
return an empty tuple. No two locations will have the same distance. 

NOTE: You cannot use the lambda function.

"""

def location_ideas(locations):
    newtuple = ()
    newlist = []
    for subtup in locations:
        subtup = subtup[::-1]
        newlist.append(subtup)
    newlist.sort()


    for sub in range(len(newlist)):
        location = (newlist[sub][1],)
        newtuple += location
    
    return newtuple

"""
Function: find_airbnb
Parameters:  airbnb list (list of tuples), number of people (int), max price (float) 
Returns: A tuple 

Description: As a broke college student, you want to be able to stay in the best airbnb as
possible but also stay in the airbnb that is affordable for you. You also want to be able to
find an airbnb that will fit you and all your friends. Write a function called find_airbnb that
takes in a list of airbnb tuples in the format (NAME, CAPACITY, RATING, PRICE_PER_NIGHT). The
airbnb must be able to fit everyone in your party and be within your price range. If multiple
apartments fit these requirements, return the one with the highest rating. No airbnbs with the
same capacity will ever have the same rating. Return a tuple with the name of the airbnb (string)
and the price that each person in your group will pay per night (float rounded to two decimal places). Also,
if no airbnbs satisfy the conditions, then return an empty tuple. 

Note: If two airbnbs are both below the price range, then you should return the one with the highest rating. 

"""

def find_airbnb(information,num,price):
    newtuple = ()
    newlist = []
    maxr = 0
    maxi = 0
    x = 0
    for subtup in information:
        (name,cap,rate,per) = subtup
        if cap >= num and per<=price:
            newlist.append(subtup)
    for air in newlist:
        if air[2] > maxr:
            maxr = air[2]
            maxi = x
        x += 1
    if len(newlist)>0:
        priceper = round(newlist[maxi][3]/num,2)
        return (newlist[maxi][0], priceper)
"""
Function: travel_buddy
Parameters: A string 
Returns: A tuple 

Description: When going on vacation, it’s always better going with your BFF, but
sometimes, it’s hard choosing your favorite. Write a function that takes in a string
containing information about multiple friends. You may assume the string may always
be formatted in this way: “Friend_Name, Friend_Level ; Friend_Name, Friend_Level ; etc.”. Using
the information given in the string, find the highest friend level, and return the friend’s name
and the friend’s level in a tuple formatted as (Friend_Name, Friend_Level).

Notes:

An empty string will never be passed in. If two friends have the same friend level, then return the friend that came last in the string


"""


def travel_buddy(friends):
    newlist = []
    friends = friends.split(";")
    newlist = friends
    maxnum = 0

    for sub in newlist:
        sub = sub.split(",")
        newtup = ()
        sub[0] = sub[0].strip()
        sub[1] = int(sub[1].strip())
        if sub[1] > maxnum:
            maxnum = sub[1]
            bff = sub[0]
    newtup = (bff,maxnum)
    return newtup
   

"""

Function name: remove_ingredients
Parameters: recipeList (list of tuples of strings), allergyList (list of strings)
Returns: list of tuples of strings
Description: You prepared a list of dishes you wanted to try while on vacation, but at the last
minute you realize your BFF is allergic to a few ingredients. You are given a recipeList which is
a list of tuples. Each tuple represents a dish and contains strings representing the ingredients
of the dish. The second parameter, allergyList, is a list of things that your friend is allergic
to. For this function, go through the ingredients for each dish (tuple) and remove the ingredients
that she/he is allergic to. Return a new list of tuples representing the modified dishes without the ingredients.

Notes: Your code should not allow capitalization to change the searching of the ingredients. So for example,
if “Spinach” is in the dish, and “spinach” is on the allergy list, the ingredient “Spinach” would be eligible
to be removed. You will need to add the original casing of the ingredients to your final list.

"""

def remove_ingredients(recipe,allergy):
    newlist = []
    for i in range(len(allergy)):
        allergy[i] = allergy[i].lower()
    for x in recipe:
        newtuple = ()
        for xx in x:
            if xx.lower() not in allergy:
                newtuple += (xx,)
        newlist.append(newtuple)
    return newlist
       
        


