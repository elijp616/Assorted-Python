"""
Georgia Institute of Technology - CS1301
HW07 - APIs and JSON
"""
__author__ = """ Elijah Peterson """
__collab__ = """ I worked with Chris Eckart on this assignment using only this semester's notes. """

import requests
from pprint import pprint

"""
Function name: currencyConverter
Parameters: country (string), money (int or float), conversionFactor (int or
float)
Returns: string indicating either that the function errored or the monetary
conversion
Description: An important aspect of traveling is money! Write a function that
takes in the name of the country you’re traveling to, the amount of money to
convert, and the conversion factor, and return a string of the format
"In [country name], $[money] USD is worth [foreign currency symbol][money times
currency factor, rounded to 2 decimal places] [three-letter foreign currency
code]." Your code should be able to handle an invalid country name and instead
of erroring, should return "[country name] is not a valid country."
"""


def currencyConverter(country, money, conversionFactor):
    place = country
    url = "https://restcountries.eu/rest/v2/name/"
    i = url + country
    result = requests.get(i)
    data = result.json()
    try:
        symbol = data[0]["currencies"][0]["symbol"]
        country = data[0]["currencies"][0]["code"]
    except:
        return "{} is not a valid country.".format(country)

    cashmoney = money *conversionFactor
    cashmoney = round(cashmoney,2)
    return "In {}, ${} USD is worth {}{} {}.".format(place, str(money),symbol,cashmoney,country)
        
#print(currencyConverter("taiwan", 88.88, 31)) 


"""
Function name: translator
Parameters: codeList (list of strings)
Returns: dictionary where key and value are both strings
Description: Travelling around the world involves learning new languages! Write
a function that takes in a list of 3-letter codes representing a country and
return a dictionary where the key is the name of the country and the value is
the name of the country in its own language. Note that this function must be
able to ignore three letter codes that do not correspond to a country without
erroring. You can assume that we will not test strings that contain numbers.
Hint: The API will output something different if the country code is not valid.
Try using pprint with a request that uses an incorrect three-letter code and see
swhat it outputs!

"""


def translator(codeList):
    newdict = {}
    for country in codeList:
        url = "https://restcountries.eu/rest/v2/alpha/"
        i = url + country
        initial = requests.get(i)
        data = initial.json()
        try:
            org = data["nativeName"]
            eng = data["name"]
            newdict[eng] = org
        except:
            pass
    return newdict
#print(translator(["JPN", "ita", "aaa"])) 

"""
Function name: nearbyLocations
Parameters: codeList (list of strings)
Returns: a list of tuples, each tuple containing floats
Description: You’ve finally eliminated the list of countries you’d like to visit
down to a few finalists and think that you’d get the most out of your money if
you could go somewhere with many other nearby places to visit. Write a function
that takes in a list of 3-letter codes representing a country, finds which
country has the most bordering countries, and returns a list of tuples
containing the latitude and longitude of its bordering countries. If there are
multiple countries with the same number of borders, use the one whose name
occurs last in the alphabet. If none of the countries have bordering countries,
return an empty list. Assume that all the country codes passed in will be valid.

Hint: You may need to request data more than once.
"""


def nearbyLocations(codeList):
    
    newlist = []
    maxname = ""
    maxcountry = 0
    for country in codeList:
        url = "https://restcountries.eu/rest/v2/alpha/"
        i = url + country
        result = requests.get(i)
        data = result.json()
        name = data["name"]
        local = data["borders"]
        if maxcountry < len(local):
            maxcountry = len(local)
            maxname = name
            neighbors = local
        elif len(local) == maxcountry and (data["name"] > maxname):
            maxname = data["name"]
            neighbors = local
            maxcountry = len(local)

    for country in neighbors:
        url = "https://restcountries.eu/rest/v2/alpha/"
        i = url + country
        result = requests.get(i)
        data = result.json()
        newtup = ()
        newtup = (data["latlng"][0],data["latlng"][1])
        newlist.append(newtup)
    return newlist
                
            

#print(nearbyLocations(["mng", "usa"])) #[(60.0, -95.0), (23.0, -102.0)] 

"""
Function name: humidityCheck
Parameters: locationsList (list of ints), maxHumidity (int)
Returns: list of strings or an error message as a string if an error occurs
Description: You have some suggestions for places to visit on your much-needed
vacation, but you don’t want to go somewhere that has too much humidity. Create
a function that takes in a list of location IDs (ints) and a max humidity (int)
and returns a list of cities (strings) that have humidities less than the max
humidity. If any of the IDs are invalid, return "[Location ID] is not a valid
ID".

Hint: Use the "Current weather data" to answer this question ("weather"
endpoint) and search by IDs

"""


def humidityCheck(locationsList, maxHumidity):
    newlist = []
    key = "57349a11d0233b2a0267d5e838d4f5dc"
    for i in locationsList:
        url = "http://api.openweathermap.org/data/2.5/weather?id={}&APPID={}".format(i,key)
        result = requests.get(url)
        data = result.json()
        try:
            humid = data["main"]["humidity"]
            city = data["name"]
            print(city)
            print(humid)
            if humid < maxHumidity:
                newlist.append(city)
        except:
            return "{} is not a valid ID".format(i)
    return newlist
#locationsList = [4180386, 4179574, 1]         
#print(humidityCheck(locationsList, 80))         
        

"""
Function name: locationTemps
Parameters: coordinatesList (list of tuples of floats)
Returns: list of tuples with the first item a string and the second item a float
Description: You are given some possible locations to visit, but you want to
know the temperatures of the locations so that you can plan accordingly. Create
a function that takes in a list of tuples that contain a latitude (float) and
longitude (float) and returns a list of tuples whose first item is the name of
the location (string) and the second item is the current temperature of that
location (float). The returned list should be sorted by temperatures from low to
high. Assume all coordinates are valid latitudes and longitudes.

Hint: Use the "Current weather data" to answer this question ("weather"
endpoint) and search by latitude and longitude. You can also use the
nearbyLocations() function to create your parameters to test!

"""


def locationTemps(coordinatesList):
    newtup = ()
    newlist = []
    key = "f6e798fb956a318bb12d7db6e1f658e6"
    for i in coordinatesList:
        url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID={}".format(i[0],i[1],key)
        result = requests.get(url)
        data = result.json()
        temperature = data["main"]["temp"]
        country = data["name"]
        newtup = (country,temperature)
        newlist.append(newtup)
        newlist.sort(key=lambda x: x[1])
    return(newlist)
#b = [(-10.0, -55.0), (-2.0, -77.5), (9.0, -80.0)]     
#print(locationTemps(b)) 

"""
Function name: typesOfWeather
Parameters: locationsList (list of ints)
Returns: dictionary with strings as keys and lists of strings as values or an
error message as a string if error occurs
Description: You want to know the types of weather of different locations so
that you can plan an amazing trip! Create a function that takes in a list of
location IDs (ints) and returns a dictionary that’s keys are types of weather
(string) and values are lists of the names of the locations (string) that have
that weather. If any of the IDs are invalid, return "[Location ID] is not a
valid ID".

Hint: Use the "Current weather data" to answer this question ("weather"
endpoint) and search by IDs

"""


def typesOfWeather(locationsList):
    try:
        newdict = {}
        for i in locationsList:
            newlist = []
            url = "http://api.openweathermap.org/data/2.5/weather?id={}&APPID=f6e798fb956a318bb12d7db6e1f658e6".format(i)
            result = requests.get(url)
            data = result.json()
            weather = data["weather"][0]["main"]
            country = data["name"]
            newlist.append(country)
            if weather not in newdict:
                newdict[weather] = newlist
            elif weather in newdict:
                newdict[weather].append(country)
        return newdict    
    except:
        return "{} is not a valid ID".format(i)
    
#locationsList = [4180386, 4179574, 4179074, 5160041, 733840]
#print(typesOfWeather(locationsList))
