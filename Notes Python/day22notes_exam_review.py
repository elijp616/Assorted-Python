# day 22 - finishing up dictionaries, test review, starting getting data from the web
#
# assume you have two dictionaries...d1 and d2
# create a new dictionary with all the pairs from each - if both dictionaries
# contain the same item, sum their values - assume all values are integers
# We will do this one next time
d1 = {'a':3,'b':4,'c':5}
d2 = {'a':1,'c':7,'d':14}
newdict = {}
for key in d1.keys():
    if key in d2:
        newdict[key] = d1[key] + d2[key]
    else:
        newdict[key] = d1[key]
for key in d2.keys():
    if key in d1:
        pass
    else:
        newdict[key] = d2[key]
print(newdict)        



# dictionary tracing
d = {1:2,2:4,3:1,4:1}
print(d[d[d[d[4]]]])

d[d[4]] += 1

print(d[d[d[d[4]]]])
e = d.copy()

# tuple tracing
print("tuples")
def tupFun(aTup, bTup):  
    (a, b) = aTup
    print(a)
    bTup = b, bTup[1]
    print(bTup)
    aTup = bTup[1], bTup[0]
    print(aTup)

tupFun((4, 7), ("Four", "Seven"))

# cloning and aliasing
a = [1,2,['a','b']]
b = a
c = a[:]
a[2][0] = 'x'

print(a)
print(b)
print(c)
print("dictionaries")
d1 = {1:1,2:2,3:[1,1]}
d2 = d1
d1[1] = 5
d2[2] = d1[1]
d1[3][0] = d1[2]
print(d1)
print(d2)
print(len(d1))
print(d2[3][0])

# referencing lists and dictionaries (they are mutable, stored as a reference to the function)

def changeMe(item):
    del item[1]

value = [1,2,3]
changeMe(value)
print(value)       # actually changed the parameter

value = {1:1,2:2,3:3}
changeMe(value)
print(value)         # actually changed the parameter



# data from the web is usually stored in lists of dictionaries
#https://ghibliapi.herokuapp.com/films
#http://makeup-api.herokuapp.com/api/v1/products.json

















