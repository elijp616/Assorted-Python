# day 23 - getting data from the web

import requests # must be installed on your computer
# allows you to send a get request to a url on the web

from pprint import pprint

webdata = requests.get("https://ghibliapi.herokuapp.com/films")
#print(type(webdata))
data = webdata.json()  # converts json web data to python data
print(type(data))

# what year was princess mononoke released?
print(data[0].keys())

for num in range(len(data)):
    if data[num]['title'].lower() == "princess mononoke":
        print(data[num]["release_date"])
        princess_url = data[num]["people"]
        print(princess_url) # a list of people urls
        # at this point, do a get request on the princess_url to
        # get a list of people urls, loop through those to get
        # a dictionary for each person

# create a list of all the people in "princess mononoke"        




