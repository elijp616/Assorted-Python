### day 8 notes - more loops, break and continue
### running sums and total
##num = 0
##while num < 10:
##    print(num)
##    num += 1
##
##for num in range(10):
##    print(num)
##
### anything you can do with a for loop, you can do
### with a while loop, but not vice versa
##school = "Georgia Tech"
##for letter in school:
##    print(letter)
##
### start with an amount of money
### allow the user to spend money until there
### is no money left
##
##money = 250
##while money > 0:
##    spend = int(input("How much does it cost?"))
##    if spend <= money:
##       money -= spend  # money = money - spend
##    else:
##        print("too expensive")
##    print("You have " + str(money) + " left.")

# two new commands, break and continue

# break - immediately jumps out of the loop
# continue - immediately goes back to the start of the loop

for num in range(100):
    if num == 7:
        break
    else:
        continue
    print(num)
print('done')

# looping with strings - counting letters
school = "Georgia Tech"
count = 0
for letter in school:
    if letter in "aeiouAEIOU":
        count += 1
print(count)        
# building a new string
# write a function called get_vowels that returns a string
# of only the vowels in school

def get_vowels(words):
    newstring = ""
    for letter in words:
        if letter in "aeiouAEIOU":
            newstring += letter  # concatenate it on the end of the string
    return(newstring)        
 
#print(get_vowels(school))                 


# try this.... remove the vowels from a string



def remove_vowels(words):
   newstring = ""
   for letter in words:
       if letter not in "aeiouAEIOU":
           newstring += letter
       else:
           newstring += "*"
   return newstring

words = "Hello World"
words = remove_vowels(words)
print(words)
           

# try this....replace the vowels in a string with * (see solution above)














