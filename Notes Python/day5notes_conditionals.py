# Day 5 - Conditionals (if statements)

# write a function that returns the cost of a movie ticket depending on age
# children under 5 get in for 9.95
# senior citizens 65 or older get in for 5.00
# everyone else gets in for 11.95


def ticket_cost(age):
    if age < 3:
        return 0
    elif age < 5:
        return 9.95
    elif age >= 65:
        return 5.00
    else:
        return 11.95

print(ticket_cost(2))
print(ticket_cost(90))
print(ticket_cost(65))
print(ticket_cost(5))

# try this...
# write a function called make_positive that changes a negative number to
# positive, and doesn't change 0s or positive numbers at all

def make_positive(num):
    if num < 0:
        return -num
    else:
        return num
        
print(make_positive(-2))
print(make_positive(0))
print(make_positive(2))

def do_stuff():
    print("Stuff")

value = do_stuff()   # prints out Stuff
print(value)          # prints out None

# return exits the function immediately


def get_math(num1):  # add 1 to the parameter, then add 2 to the parameter
                    # then return the final value
     temp = num1 + 1
     return temp + num1 + 2

print(get_math(3))

# try this one
# write a function that returns 100 if the parameters are the same
# and returns 0 if the parameters are different

def check_params(num1,num2):
    if num1 == num2:
        return 100
    else:
        return 0

print(check_params(3,5)) # print 0
print(check_params(3,3))  # print 100

# write a function that returns True if the parameters are the same and False if
# they aren't the same - call this function are_same
def are_same(num1,num2):
    if num1 == num2:
        return True             # True and False must be capitalized in python
    else:
        return False





    
                    
    
    

