"""
Georgia Institute of Technology - CS1301
Extra Credit HW
"""

__author__ = """ Elijah Peterson """
__collab__ = """ I worked on this assignment alone """

"""
Function name: date_cruncher
Parameters: original_dates (list of strings)
Returns: list of strings
"""


def date_cruncher(original):
    monthdict = {"january":"01","february":"02","march":"03","april":"04","may":"05","june":"06","july":"07","august":"08",
                 "september":"09", "october":"10", "november":"11", "december":"12"}
    newlist = []
    numlist = []
    daylist = []
    yearlist = []
    complete = []
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    for i in range(len(original)):
        end = original[i].find(" ")
        letters = original[i][:end].lower()
        newlist.append(letters)
        end2 = original[i].find(",")
        if original[i][end+1:end2] in numbers:
            pre = original[i][end+1:end2]
        elif original[i][end+1:end2-1] not in numbers:
            if original[i][end+1:end2-2] not in numbers:
                pre = original[i][end+1:end2-2]
            else:
                pre = original[i][end+1:end2-2]
        if len(pre) == 1:
            pre = "0" + pre
        end3 = end2 + 2
        year = original[i][end3:]
        daylist.append(pre)
        yearlist.append(year)
    for x in newlist:
        for i in monthdict:
            if x == i or x == i[0:3]:
                num = monthdict[i]
                numlist.append(num)
    for i in range(len(original)):
       newstring = ("{}-{}-{}".format(numlist[i],daylist[i],yearlist[i]))
       complete.append(newstring)
    return(complete)
    
aList = ["dEcEmBER 3, 2020", "FEB 31st, 6000", "apR 5, 1776"] 



"""
Function name: honor_roll()
Parameters: students (list of tuples)
Returns: tuple of lists
"""


def honor_roll(students):
    finaltup = ()
    highest = []
    high = []
    honor = []
    newdict = {}
    

    
    for i in students:
        total = 0
        name,grade = i
        for i in grade:
            total += i
        average = total/len(grade)
        newtup = average,name
       
        if average >= 95:
            highest.append(newtup)
        if average >= 90 and average < 95:
            high.append(newtup)
        if average >= 80 and average < 90:
            honor.append(newtup)
    

    highest.sort(reverse = True)
    high.sort(reverse = True)
    honor.sort(reverse = True)
    newhigh = []
    newhighest = []
    newhonor = []

    for i in honor:
        newhonor.append(i[1])
    for i in high:
        newhigh.append(i[1])
    for i in highest:
        newhighest.append(i[1])

    return(newhighest, newhigh, newhonor)

        
aList = [("A",[2]), ("B", [97]), ("C", [89]), ("D", [90]),("E",[83]),("F",[92]),("G",[95])] 

"""
Function name: spotify_recs()
Parameters: my_library (dict), new_songs (list of dicts)
Returns: list of strings
"""


def spotify_recs(my_library, new_songs):
    pass


"""
Function name: state_data
Parameters: filename (str), state (str)
Returns: tuple (num of schools (int), avg. cost of enrollment for 4 years (float),
                avg. cost (float), avg. SAT score (float))
"""


def state_data(filename, state):

    f1 = open(filename, "r")
    heading = f1.readline()
    data = f1.readlines()

    count = 0
    enroll = 0
    cost = 0
    sat = 0

    for i in data:
        i = i.split(",")

        new = i[2].lower()
        if new == state.lower():
            count += 1
            
            cost += float((i[8])*4)
            enroll += float(i[5])
            sat += float(i[10].strip())
    if count == 0:
        return (0,0,0,0)

    else:
        avenroll = enroll/count
        avenroll = round(avenroll,2)
        avcost = cost
        avcost = round(avcost,2)
        avsat = sat/count
        avsat = round(avsat,2)

    return(count,avenroll,avcost,avsat)


    


"""
Class name: Sandwich
Description: See PDF for instructions
"""


class Sandwich:
    def __init__ (self,meats,veggies, bread_slices = 2):
        self.meats = meats
        self.veggies = veggies
        self.bread_slices = bread_slices
        if len(meats) == 0:
            self.vegetarian = True
        else:
            self.vegetarian = False

    def favorite(self,fave_ingredients, required_num):
        ingredients = []
        for i in self.meats:
            ingredients.append(i)
        for i in self.veggies:
            ingredients.append(i)

        meat = 0
        veg = 0

        for i in fave_ingredients:
            if i in self.meats:
                meat += 1
            if i in self.veggies:
                veg += 1

        total = meat + veg

        if total >= required_num:
            return ("You would like this sandwich! It has {} of your favorite meats and {} of your favorite veggies!".format(meat,veg))
        else:
            if len(fave_ingredients) == 0:
                return (Sandwich([],[],required_num))
            else:
                return Sandwich([fave_ingredients[0]],[],required_num)

    def merge(self,other):
        protein = self.meats
        weak = self.veggies

        for i in other.meats:
            if i not in protein:
                protein.append(i)
        for i in other.veggies:
            if i not in weak:
                weak.append(i)

        breads = self.bread_slices + other.bread_slices
        return Sandwich(protein,weak,breads)
        
            
        
        


"""
Function name: sum_row
Parameters: row (list of ints)
Return value: sum of the ints in row (int)
"""


def sum_row(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_row(array[1:])


"""
Function name: sum_col
Parameters: array (list of lists), col (int), index (int, default to 0)
Return value: sum of the ints in col (int)
"""


def sum_col(array, col, index=0):
    if len(array) == 0:
        return 0
    else:
        return array[0][col] + sum_col(array[1:],col,index = 0)


"""
Function name: sum_diag
Parameters: array (list of lists), index (int, default to 0)
Return value: sum of the ints in diagonal (from [0, 0] to [N, N]) (int)
"""


def sum_diag(array, index=0):
    if len(array) == 0:
        return 0
    else:
        return array[0][index] + sum_diag(array[1:], index = index + 1)


"""
Function name: sum_reverse_diag
Parameters: array (list of lists), index (int, default to length of array - 1)
Return value: sum of the ints in diagonal (from [0, N] to [N, 0]) (int)
"""


def sum_reverse_diag(array, index=None):
    if index is None:
        index = len(array) - 1


"""
Function name: magic_square
Parameters: array (list of lists), target (int), index (int, default to 0)
Returns: boolean
"""


def magic_square(array, target, index=0):
    pass
