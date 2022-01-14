 # day 9 - indexing through strings using loops
 # today we start chapter 8
 # strings are our first compound data type

# first three letters of spongebob
print("spongebob"[0:3])  # slicing

#for letter in "spongebob"     # won't work - only does all the letters

for number in range(0,3):
    print("spongebob"[number],end="")  # indexing in a loop

# print out only the first 5 letters of spongebob if they are vowels

for number in range(0,5):
    if "spongebob"[number] in "aeiouAEIOU":
        print("spongebob"[number],end="")
print()    


# loop through a string looking for a particular character
def find_char_old(phrase, character):
    place = 0
    for letter in phrase:
        if letter == character:
            print("Found it at location " + str(place))
        place += 1    

def find_char(phrase, character):
    for number in range(len(phrase)):
        if phrase[number] == character:
            print("Found it at location " + str(number))
find_char("I love cs"," ")











    

