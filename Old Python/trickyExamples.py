'''
Some tricky examples!
'''
a  = [1,3,5,2,4]
a.sort() 
print(type(a))

##.sort() modifies actual list but returns None. Same for all methods that act on lists

a  = [1,3,5,2,4]
a = a.sort() 
print(type(a))

print("~~~~~~~~~~~~~~~~~~~~~")

##If you see a print statement, PRINT! Same goes for all functions
a = {print("Hello World"): 2, 3: 9} ##print returns None (type: NoneType)!
print(a[None])
a[print("Still prints")] = 4
print(a)

print("~~~~~~~~~~~~~~~~~~~~~")

print(3.0 == 3) ##Use == for equality and = for assignment
print(bool(33983042))
print(bool(0))
try:   
    a = [1,2,3]
    a[2.0]  ##although 2.0 == 2, indexing takes in an INT!
except:
    print("Use ints for indexing and slicing")

print("~~~~~~~~~~~~~~~~~~~~~")

for i in range(10, 3, 2): ##Will NOT error, it just won't execute
    print("Negative step in order to go backwards")

for i in range(2,2,1): ##Will NOT error, it just won't execute
    print("But the 2 is inclusive??")

print("~~~~~~~~~~~~~~~~~~~~~")

a = "Hello World"
print("Length of 'Hello World': " + str(len(a)))
print(a[len(a) - 1]) ##The largest index is len(theString) - 1
try:
    a[2.0:]##although 2.0 == 2, slicing takes in an INT!
except:
    print("Use ints for indexing and slicing")
    
print(a[:-2]) ##Negative indices start from -1 and refers to the last character

print(a[2:-2:-1]) ##prints empty string because the character a index -2 is after the character at index 2

print(a[1:33243242]) ##slicing will NOT throw an index out of bounds error.

print(a[23132:231232]) ##prints empty string because these indices are not valid for this string

print(a[-2:1:-1]) ##don't get confused by the negatives, look at PLACEMENT in the string

print("~~~~~~~~~~~~~~~~~~~~~")

a = (1,[2,3,4])
a[1][2] = 5 ##VALID because I am changing a MUTABLE data type: a list
print(a)
try:
    a[1] = 4 ##INVALID because I am changing an IMMUTABLE data type: a tuple
except:
    print("I tried to change the tuple not the list")


print("~~~~~~~~~~~~~~~~~~~~~")

a= [1,2,3,[4,5,6]]
b= a[:] ## b is a CLONE of a
c = b ##c is an ALIAS of b

##Changes made to b will be shown in c. Changes made *INSIDE* the nested list will be shown in all lists.

a[0] = 0
b[0] = 10
a[3][1] = 8
b[3][2] = 9
c[3][0] = 7
print(a)
print(b)
print(c)
a[3] = 4 ##I am not changing anything *INSIDE* the nested list so it will not show in both b and c
print(a)
print(b)
print(c)

print("~~~~~~~~~~~~~~~~~~~~~")
