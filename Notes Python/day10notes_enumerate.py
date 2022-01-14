# Day 10 - enumerate, a few string methods, strings are immutable, count digits example
place = 0
word = "beat"
for letter in word:
    print(letter + " was found at " + str(place))
    place += 1

# we could do this an easier way using the enumerate function
for (place,letter) in enumerate(word):
    print(letter + " was found at " + str(place))
    

# methods are functions that are called using dot notation
print(word.upper()) # strings cannot be changed! they are immutable
word = word.upper()
#word[0] = "z" runtime error!
word = "z" + word[1:] # you must build a new string
print(word)

# strings are immutable - they can't be changed
# replace the first letter of the word with a z
#word[0] = "z"
#word = "z" + word[1:]

word.replace("a","-") # the replace method makes a new string
print(word)
word = word.replace("a","---")
print(word)


# mini quiz answers

def nickname(name, num):
    newstring = ""
    for letter in range(0,num):
        for i in range(0, letter+1):
            newstring += name[letter]
        return newstring

def nickname2(name,num):
    newstring = ""
    for letter in range(0,num):
        newstring += name[letter] * (letter +1)
    return newstring
