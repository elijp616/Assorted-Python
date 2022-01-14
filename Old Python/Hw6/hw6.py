def make_gamertag(start,index):
    newstring = ""
    for i in index:
        try:
            newstring += start[i] + "x"
        except:
            newstring += "0"

    newstring = "[" + newstring + "]"
    return newstring

thing = [20, 4, 50, 0, -2, 3]
thing2 = "Aw Geez Rick"
test = make_gamertag(thing2,thing)

def split_the_loot(store,stolen,cash,burg):
    total = 0
    try:
        for i in store:
            for x in stolen:
                if i == x and store[i]<0:
                    return "Negative"
                elif i==x:
                    total += store[x]
    except TypeError:
        return("TypeError")

    if burg > 0:
        
        money = total + cash
        split = round(money/burg,2)
        return split
    elif burg <= 0:
        return "BurglarErorr"
   

aDict = {"eli" : "d", "Celery": -1.2, "Gum": 5}
items = ["Celery", "Gum"]
cash = 12310.32
burglars = 5
loot1 = split_the_loot(aDict, items, cash, burglars)
            
            
def football_stars(teams,players):
    newdict = {}
    for i in teams:
        for x in players:
            if x in teams[i]:
               newdict[players[x]] = (x,i)
    return newdict
    
locations = {"Arizona": ["Cardinals"], "New York": ["Giants", "Jets", "Bills"], "Ohio": ["Bengals", "Browns"]}
teams = {"Giants": "OBJ", "Cardinals": "David Johnson"}
stars = football_stars(locations,teams)

def pair_rivals(one,two):
    newdict = {}
    newtup = ()
    for a in one:
        for b in one:
            if a == one[b]:
                newtup += a,
    
    for x in one:
        for i in two:
            if x == two[i] and x not in newtup:
                newtup += x,
            if  one[x] == i and i not in newtup:
                newtup += i,
    for c in two:
        for d in two:
            if c == two[d] and c not in newtup:
                newtup += c,
            
    if newtup != ():
        newdict[newtup] = True
        return newdict
    else:
        return newdict

a = {"Regina": "Cady", "Superman": "Zod", "Cady": "Regina"}
b = {"Zuko": "Cady", "Batman": "Joker" ,"Bob": "Batman"}
rivals1 = pair_rivals(a, b)
                
def zoo_keeper(animals):
    newdict = {}
    
    for i in animals:
        newdict2 = {}
        for tp, spec, num in animals:
            for tp2, spec2, num2 in animals:
                if tp not in newdict:
                    newdict[spec] = num
                    newdict[tp] = newdict2
                if tp2 == tp and tp in newdict:
                    newdict2[spec2] = num2
                    newdict[tp] = newdict2
                
                    
                
   

list2 =[('mammal', 'doge', 4), ('reptile', 'python', 37), ('bird', 'chicken nugget', 8), ('mammal', 'clifford', 2),
        ('reptile', 'python', 3), ('bird', 'eagle', 1), ('mammal', 'harambe', 0)]            

zoo2 = zoo_keeper(list2)
print(zoo2)

            
