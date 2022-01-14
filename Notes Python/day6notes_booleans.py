# day 6
# advanced conditionals and booleans
##
##answer = 5 > 2  
##print(answer)
##print(type(answer))
##
##if answer or 2 < 7:
##    print("stuff")
##
### precendence of boolean operations  not, and, or
##
##
##
### arithmetic operations, < >, not and or
### happen before boolean operations
##
##print(3 + 5 < 7 or not 7-2<3)

num = 0  # any value other than None, False, 0, 0.0, "" result in True
if num:
    print("really?")

# functions that return a boolean value

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

age = int(input("Enter your age"))
if is_even(age):
    print("Your age is even")
else:
    print("You are odd")

# nested if statements
number = 1
if number > 0:
    if is_even(number):
        print("Even number")
    else:
        print("Odd number")
else:
    print("not a positive number")

# be able to tell what test cases would work correctly for given code
# in the one above, only positive even numbers work correctly

# rewrite the code above, (correctly) with and/or not nested
number = 1
if number > 0 and is_even(number):
        print("Even number")
elif number > 0 and not is_even(number):
    print("Odd number")      
else:
    print("not a positive number")
    

# short circuit evaluation
# an if statement only checks as far into the boolean expression
# as needed to determine True or False
if 3>2 or 5 < 2:
    print("stuff")

if 3 < 2 and 4 / 0 > 99:
    print("*")
else:
    print("no divide by zero")
    

mynum = 3
if mynum != 0 and 99/mynum > 33:
    print("whatever")

# coding practice

# write a function called double_or_triple that returns 2 times
# the integer parameter if it is even and 3 times if it is odd
# you must use is_even


print(double_or_triple(3))
print(double_or_triple(-2))





