# day 24 - more APIs - not in the textbook
import requests
from pprint import pprint

# api - application programming interface - a way to share data and code
# among programmers

# some api's require a key - for most this is simply a matter of signing up

baseURL = "https://www.metaweather.com"
fullURL = baseURL + "/api/location/search/?query=atlanta"

# first find atlanta
r = requests.get(fullURL) # r is a request object - response code 200 is good
#print(type(r))
data = r.json() # converts json data to python
print(data)
woeid = data[0]['woeid']
print(woeid)
print(type(woeid))

# now search for the weather

atlantaURL = baseURL + "/api/location/" + str(woeid)
r = requests.get(atlantaURL)
data = r.json()
#print(data)
#pprint(data['consolidated_weather'][0]['max_temp'])


# which of the cities in this list passed in as a parameter has the
# current highest temperature
def hottestCity(city_list):
    baseURL = "https://www.metaweather.com/api/location/search/?query="
    maxtemp = -5000
    maxcity = "no name"
    for city in city_list:
        fullURL = baseURL + city
        r = requests.get(fullURL)
        data = r.json()
        woeid = data[0]['woeid']
        cityURL = "https://www.metaweather.com/api/location/" + str(woeid)
        r = requests.get(cityURL)
        data = r.json()
        city_temp = data['consolidated_weather'][0]['the_temp']
        if city_temp > maxtemp:
            maxtemp = city_temp
            maxcity = city
    return maxcity       

        
        
        


print(hottestCity(['atlanta','chicago','tokyo','lima']))
      
            




