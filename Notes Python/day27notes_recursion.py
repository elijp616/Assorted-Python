# day 27 - more csv files and recursion
##
##f = open("crime_data.csv","r")
### did district 1 or district 2 have more crime
##headings = f.readline()
##data = f.readlines()
##f.close()
##count1 = 0
##count2 = 0
##for line in data:
##    line = line.split(",")
##    district = line[1]
##    if district == "1":
##        count1 += 1
##    elif district == "2":
##        count2 += 1
##if count1 > count2:
##    print("District one")
##elif count2 > count1:
##    print("District two")
##else:
##    print("same")
##
### which district had the most crime?
##f = open("crime_data.csv","r")
##headings = f.readline()
##data = f.readlines()
##f.close()
##dict = {}     # i can do this, but now I can't use the dict( ) function at all
##for line in data:
##    line = line.split(",")
##    district = line[1]
##    if district in dict:
##        dict[district] += 1
##    else:
##        dict[district] = 1
##highestvalue = 0        
##for (key,value) in dict.items():
##    if value > highestvalue:
##        highestvalue = value
##        highdistrict = key
##print(highdistrict + " is most crime-ridden.")        


# recursion

# instead of loop for repetition we write a function that calls itself which
# makes it start over again at the beginning until you get to a base case - a
# question you already know the answer to

# 3 rules:
# the function must call itself
# function must have a base case
# each recursive call must be closer to the base case


def count_down(num):
    if num <= 0:
        pass
    else:
        print(num)
        count_down(num - 2)

count_down(11)        


def sum_numbers(num):
    if num == 1:
        return 1
    else:
        return num + sum_numbers(num - 1)

print(sum_numbers(27))


# print all the odd numbers from the parameter down to 1

def print_odds(num):
    if num == 1:
        print(num)
    else:
        if num%2 == 1:
            print(num)
            print_odds(num-2)
        else:
            print_odds(num-1)

print_odds(10)            
            

            


            











