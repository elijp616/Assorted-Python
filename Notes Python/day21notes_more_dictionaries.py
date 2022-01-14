# day 21 - more dictionaries

d = {"apples": 15, "bananas": 35, "grapes": 12}
print(d["bananas"] + len(d.keys()))    # what will this print? 38

# dictionary tracing
d = {"apples":(15,5), "bananas":{3:5,6:7}, "grapes":[12,14,16]}
print(d['apples'][1] +d['bananas'][len(d['grapes'])])

d = {'a':(2,3),'b':[4,5]}
e = d

print(e['a'][1] + d['b'][0])




# creating a dictionary from text

data = "This is the song that never ends. It just goes on and on my friends."

# i want a dictionary that keeps track of how many of each letter are in the data

d = {'t':3,'h':1,'i':2}

import string
data = data.lower()
newdata = ""
for ch in data:
    if ch in string.ascii_letters:   
        newdata += ch
        
print(newdata)
d = {}
for letter in newdata:
    if letter in d:   # do not put d.keys() it is inefficient
       currentvalue = d[letter]
       d[letter] = currentvalue + 1
    else:    
       d[letter] = 1
print(d)    
    
# practice coding 1
# total the number of the counts of the letters in this list by looking them
# up in d
total = 0
letters = ['a','b','c','e']
for letter in letters:
    if letter in d:
        total += d[letter]
print(total)

# redo the text example above, but adding words and their frequencies to
# d instead of the letters
#{'this':1,'is':1,'the':1,'song':1,'on':2.....



data = "This is the song that never ends. It just goes on and on my friends."

# i want a dictionary that keeps track of how many of each letter are in the data

import string
data = data.lower()
newdata = ""
for ch in data:
    if ch not in string.punctuation:   
        newdata += ch       
print(newdata)
newdata = newdata.split()  # a list of words
d = {}
for word in newdata:
    if word in d:   # do not put d.keys() it is inefficient
       currentvalue = d[word]
       d[word] = currentvalue + 1
    else:    
       d[word] = 1
print(d)  


# dictionaries are mutable
# dictionaries are reference variables


d2 = d  # alias

d2['hello'] = 7


print(d)









# practice coding 2











