import rate
def yelp_rating(orginal,num,operation):
    orginal = float(orginal)
    num = float(num)
    if operation == "+":
        new = rate.add(orginal,num)
    elif operation == "-":
        new = rate.subtract(orginal,num)
    elif operation == "*":
        new = rate.multiply(orginal,num)
    elif operation == "/":
        new = rate.divide(orginal,num)
    else:
        return None
    new = round(new,1)
    return new

print(yelp_rating(2.0,3.0,"/"))


def register_passport(info):
    name = ""
    age = ""
    country = ""
    namerng = info.find(":")
    for x in info[0:namerng]:
        name += x
    agerng = info.find(",")
    for i in info[namerng+1:agerng]:
        age += i
    for z in info[agerng+1:]:
        country += z
    age = age.strip()
    age = int(age)
    country = country.strip()
    b =(country,name, age)
    return(b)
test1 = register_passport("Catilin Yang: 19, USA")
print(test1)
    
def location_ideas(locations):
    newtuple = ()
    newlist = []
    for subtup in locations:
        subtup = subtup[::-1]
        newlist.append(subtup)
    newlist.sort()


    for sub in range(len(newlist)):
        location = (newlist[sub][1],)
        newtuple += location
    
    return newtuple
        

aList = [("Paris, France", 4370), ("Shanghai, China", 12290), ("Quebec, Canada", 2207),("Orlando, Florida", 440)]
test1 = location_ideas(aList)
print(test1)


def find_airbnb(information,num,price):
    newtuple = ()
    newlist = []
    maxr = 0
    maxi = 0
    x = 0
    for subtup in information:
        (name,cap,rate,per) = subtup
        if cap >= num and per<=price:
            newlist.append(subtup)
    for air in newlist:
        if air[2] > maxr:
            maxr = air[2]
            maxi = x
        x += 1
    if len(newlist)>0:
        priceper = round(newlist[maxi][3]/num,2)
        return (newlist[maxi][0], priceper)
           

list1 = [("Hawaiian Luau",10,4.5,500), ("Hawaiian Mist",7,3.5,350),("Mountain Melody",2,5.0,600),("North Ave Apartments",15,1,200)]
test1 = find_airbnb(list1,6,400)
print(test1)
        
            
def travel_buddy(friends):
    newlist = []
    friends = friends.split(";")
    newlist = friends
    maxnum = 0

    for sub in newlist:
        sub = sub.split(",")
        newtup = ()
        sub[0] = sub[0].strip()
        sub[1] = int(sub[1].strip())
        if sub[1] > maxnum:
            maxnum = sub[1]
            bff = sub[0]
    newtup = (bff,maxnum)
    return newtup
   
        
    
test1 = travel_buddy(("Natalie, 500 ; Tiffany, 501 ; Jason, 88 ; Peter, 0 ; Sunny, 30"))
print(test1)
        
    
def remove_ingredients(recipe,allergy):
    newlist = []
    for i in range(len(allergy)):
        allergy[i] = allergy[i].lower()
    for x in recipe:
        newtuple = ()
        for xx in x:
            if xx.lower() not in allergy:
                newtuple += (xx,)
        newlist.append(newtuple)
    return newlist
       
        


recipeList = [('Turkey', 'cheese', 'spinach'), ('CHICKEN', 'onions', 'sugar'), ('pork', 'oregano', 'bread')]
allergyList = ['brussel sprouts', 'OREGANO', 'Bell Peppers', 'onions', 'Spinach']  
remove_ingredients(recipeList,allergyList)    
            
        
        

