# day 11 - string methods, intro to lists

# methods find, split, strip, replace, lower, upper
word = "go jackets a a"
print(word.find("a"))

word = word.replace("a","z")
print(word)

myword = " go jackets    "
myword = myword.strip()  # strips off whitespace from beginning and end
print(myword)


stuff = "cat\ndog"
for letter in stuff:
    print(letter)
print(len(stuff))


# split splits a string into a list of individual pieces
sentence = "the fat    cat\nsat on the      hat"
wordlist = sentence.split() # splits on any amount of whitespace
word4 = wordlist[3]
letter2 = word4[1]
print(letter2)


print(wordlist)

for word in wordlist:
    print(word)

# print out the second letter of the fourth word of sentence
print(wordlist[3][1])

# split on a different character

phone = "770-365-5432"
numberlist = phone.split("0")
print(numberlist)

# useful string constants
import string

print(string.digits)
print(string.ascii_uppercase)
print(string.punctuation)
print(string.ascii_lowercase)
print(string.ascii_letters)

# remove all the punctuation from the parameter, return the string without
# any punctuation


def clean_up(astring):
    newstring = ""
    for letter in astring:
        if letter not in string.punctuation:
            newstring += letter
    return newstring

sentence = "the fat, cat, and the big, egg"
sentence = clean_up(sentence)
print(sentence)
    
    















    

    
