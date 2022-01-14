# Day 13 - Advanced Lists

##grades = [77,88,99,-10,100,0]
##
##if 100 in grades:
##    print("good class")
##    
### find the highest grade
##highest_so_far = grades[0] # standard way to do it
##for grade in grades:
##    if grade > highest_so_far:
##        highest_so_far = grade
##
##print(highest_so_far)        
##
### del, remove, append, etc. actually change the list
##grades = [77,88,99,-10,100,0]
### deleting from the list
##del grades[0]  # deletes at that index
##grades.remove(0)  # removes the first value 0 found or throws an error
##
##print(grades)
##
### practice tracing
##print(grades[3])
##del grades[1]
##print(grades[2])
##
##newlist = grades[1:3]  # a slice of the old list
##print(newlist)
##
##grades.append(99)
##print(grades)

# nested lists
products = [['1-2','2-2'],['55-1','55-a','55-3'],['8-8']]
##print(len(products))
##print(len(products[1]))
##print(products[1][1].upper())


# print out a nested list

for alist in products:
   for item in alist:
       print(item, end = " ")
   print()  # go down a line
       



       
##    
### try to do this....write a function that returns
### a new list that contains every item from
### a list of lists
##def getList(alist):
##   newlist = []
##   for smalllist in alist:   
##       for item in smalllist:
##           newlist += item # concatenation 
##           print(item)
##           print(newlist)
##   return newlist        
##
##
##print(getList(products))
###['1-2','2-2','55-1','55-a','55-3']  # output
##
##
























    

