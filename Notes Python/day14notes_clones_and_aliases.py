# Day 14 - List cloning and aliasing (11.9)

# lists are stored differently than primitive variables

# the variable name is only a reference to where the list is stored - not a value

alist = [1,2,3]
blist = [4,5,6]
clist = alist   # alist and clist share the address of the list

alist.append(23)
clist.append(23)
print(alist)

dlist = blist
del dlist[0]

print(len(blist))


aalist = [1,2]
bblist = [3,4]
cclist = bblist
ddlist = cclist + bblist   # makes a new list
aalist.append(2)
bblist.append(2)
cclist.remove(2)  
print(len(ddlist))

# make an identical copy or a clone (not an alias)

alist = [1,2,3]
blist = [2,3,4]
clist = alist[:]    # copy all the items from alist into clist
dlist = blist     # an alias

clist.append(999)  # doesn't change alist
dlist.append(999)   # does change blist

elist = alist + []  # makes a new list
elist.append(999) # doesn't change alist

print(len(alist))
print(len(blist))
print(len(clist))

# list algorithms chapter 14


# last time we discussed the algorithm for finding the max

# find the most frequent item in a list with duplicates
alist = [1,2,3,2,3,4,3,2,1,1,8,1,1,6]

most = 0
item = alist[0]
for i in alist:
    count = 0
    for compare in alist:
        if i == compare:
            count += 1
    if count > most:
        most = count
        item = i
print("{} occurred the most with {} times.".format(item,most))        


# given two lists, return the count of how many items
#n are in both lists at the same place
# you can't assume they are the same length
def count_same(alist,blist):
    count = 0
    place = 0
    while place < len(alist) and place < len(blist):
        if alist[place] == blist[place]:
            count += 1
        place += 1
    return count       
            



print(count_same([1,2,3,4,0],[0,2,4,4]))   # prints 2
    































