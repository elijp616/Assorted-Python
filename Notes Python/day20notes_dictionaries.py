# Day 20 - dictionaries

##def func(x):
##    try:
##        x = x/(x-1)
##        print(x)
##        print(wow)
##    except:
##        print("an error occurred")
##    finally:
##        print("the code is complete")
##
##alist = [1,2,0,4]
##for item in alist:
##    func(item)

# dictionaries

# you cannot index into a dictionary
# it is a set of key:value pairs
# keys can be any immutable data type - string, tuple, int, float, boolean, None
# values can be any data type including the above and also lists, dictionaries....
# keys must be unique in the dictionary, 


fooddict = {'bread':2.99, 'milk':3.49, 'eggs':4.29}

print(fooddict['bread'])  # look up the value associated with the key 'bread'

# add to a dictionary by creating a new key:value pair
fooddict[83] = 99
# replace a value in a dictionary by creating a new key:valuye pair
fooddict['bread'] = 1.99

print(fooddict)


# dictionary methods  .keys()   .values()    .items() - pairs
print(fooddict.keys())
print(type(fooddict.keys()))  # an enumerated data type

for key in fooddict:
    print(fooddict[key])  # prints the value

del fooddict['bread']
print(fooddict)
if 'mlkkk' in fooddict:  # looks at the keys of the dictionary
    del fooddict['mlkkk']

print(4.29 in fooddict) # looks it up    

for thing in ['bread','milk','eggs',83]:
  try:
    del fooddict[thing]
  except:
    pass



print(fooddict)


# create a dictionary from 2 lists
alist = [1,2,3]
blist = [4,5,6]

newdict = {}
for count in range(len(alist)):
    newdict[alist[count]] = blist[count]
print(newdict)    
    









            
    
        
    
