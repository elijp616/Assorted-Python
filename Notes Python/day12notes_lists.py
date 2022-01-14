# day 12 notes - lists - chapter 11
# announcement - review session tonight from 6 to 8 in this room
# on exams, you do not have to handle any cases not described in the program
# description

# lists are a compound data structure that can hold non-homogeneous data types

mylist = ['a','b','cat',9.4,False,[1,2,3]]
for item in mylist:
    print(type(item))
    
grades = [99,98,99.5,97,100]
grades += [70] # concatenating two lists
grades *= 2
print(grades)


total = 0
for num in grades:
    total += num
print(total/len(grades))    

print(100 in grades)

# adding to a list
grades.append(70) # lists are mutable
# list methods actually change the list
# but don't return anything (except None)
print(grades)


grades.remove(70) # removes a value
print(grades)

del grades[0]   # removes at an index
print(grades)


# insert at a specific location
letters = ['a','b','d','f']

letters.insert(2,'c')
print(letters)

# be careful using for loops with lists
grades = [70,98,99,100,99,97]
# add 3 points to all the grades
for item in grades:
    item += 3
    print(item)
print(grades)

for num in range(len(grades)):
    grades[num] += 3
print(grades)

# write a function called makecopy that
# returns an identical copy of a list

def makecopy(alist):
    newlist = []
    for item in alist:
        #newlist.append(item)
        newlist += [item]
    return newlist    

print(makecopy( [3,4,5,6]))

def makecopy2(alist):
    return alist

print(makecopy2( [3,4,5,6]))
anotherlist = makecopy([3,4,5,6])
print(anotherlist)


# a list is stored in memory as a pointer
# to the first item in the list

grades = [88,99]
grades2 = grades

print(grades)
print(grades2)
grades.append(84)
print(grades)
print(grades2)

# try this...
# write a function makeplural that
# takes a list of strings and makes each
# of them plural

def makepluralold(alist):
    for num in range(len(alist)):
        alist[num] += 's'
    return alist    

def makeplural(alist):
    newlist = []
    for item in alist:
        item += 's'
        newlist.append(item)
    return newlist

print(makeplural(['cat','dog','bird']))


















