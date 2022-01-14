"""
Georgia Institute of Technology - CS1301
HW08 - File I/O
"""
__author__ = """ Elijah Peterson """
__collab__ = """ I worked on this assignment alone using only this semester's materials. """

"""
Function name: get_roster
Parameters: filename (string)
Returns: Read in a file of any name, but assume it is in the format stated
above. Go through every line and make a list of tuples of all the students
in the class. The tuples will be formatted (FirstName, LastName). Return this
list. If the file is not found, catch a FileNotFoundError and return
“File is not found.” 
"""
def get_roster(filename):
    try:
        newlist = []
        f1 = open(filename, "r")
        data = f1.readlines()
        f1.close()
        for i in data:
            i = i.strip()
            if "," in i:
                newtup = ()
                end = i.find(",")
                first = i[:end]
                last = i[end+2:]
                newtup = first,last
                newlist.append(newtup)
               
        return newlist
            
    
    except FileNotFoundError:
        return("File is not found.")
    
    
    

#students = get_roster("students.txt")


"""
Function name: get_average
Parameters: filename (string), student (string)
Returns: A tuple with the name of the student (without the comma)
and their average for their exams
Description: Read in a file of any name but in the format as what is stated
above. For the student passed into the function, find the student and take
the average of their test scores. The average will be a float rounded to two
decimals. Return this data as a tuple in the format
(FirstName LastName, Average). If the student is not found in the file,
return “Student not found in file.”. If the file is not found, catch a
FileNotFoundError and return “File is not found.” 
"""
def get_average(filename, student):
    try:
        f1 = open(filename,"r")
        data = f1.readlines()
        f1.close()
        newlist = []
        newtup = ()
        total = 0
        place = 0
        for i in student:
            space = student.find(" ")
            first = student[:space]
            last = student[space+1:]
            newstudent = first + ", " + last
        for x in data:
            x = x.strip()
            if newstudent not in x:
                place += 1
            if newstudent in x:
                for xx in data:
                    if place+1 < len(data):
                        if ":" in data[place+1]:
                            scores = data[place+1].strip()
                            newlist.append(scores)
                            place +=1
        for individual in newlist:
            end = individual.find(":")
            percent = individual[end+2:]
            total += float(percent)
            average = round(total/(len(newlist)),2)
        newtup = student,average
        return newtup       
    except FileNotFoundError:
        return "File is not found."
    except:
        return "Student not found in file."
                
            

        
#student_average = get_average("students.txt", "Jasmine Yap")

"""
Function name: get_all_averages
Parameters: filename (string)
Returns: A dictionary representing a student as the key,
and their average on exams as the value
Description: Read in a file of any name but in the format as what is stated
above. For every student, make an entry in a dictionary where their first
name is the key and their average for their exams as the value. The file will
not have duplicate first names. The average will be a float rounded to two
decimals. If the file is not found, catch a FileNotFoundError and return
“File is not found.” 
"""
def get_all_averages(filename):
    try:
        newlist = []
        newdict = {}
        scores = []
        f1 = open(filename,"r")
        data = f1.readlines()
        for i in data:
            i = i.strip()
            if "," in i:
                newtup = ()
                end = i.find(",")
                first = i[:end]
                last = i[end+2:]
                name = first + " " + last
                newlist.append(name)
        for i in newlist:
            scores.append(get_average(filename, i))
        for x in scores:
            name,num = x
            name = name.strip()
            stop = name.find(" ")
            first = name[:stop]
            newdict[first] = num
        return newdict
    except FileNotFoundError:
        return "File is not found."


#averageDict = get_all_averages("students_tester.txt")
#print(averageDict) 

"""
Function name: form_groups
Parameters: filename (string), current_student (string), num_per_team (int)
Returns: None
Description: Read in a file of any name but in the format as what is stated
above. If the file is not found, catch a FileNotFoundError and return
“File is not found.”. In a new file to write named group.txt, write
“Team StudentName” on one line, replacing StudentName with the name of the
current student passed in. Go through the file to find the top X-1 number
of students to add to your team, top being those with the highest averages.
X is the number passed in representing the maximum number of people per team,
and X-1 is the number of students selected on the team minus the current
student. The current student can not be one of the students added to the team.
If there are less than X number of students, then everyone in the file is
included on the team. However, the number of students in a team can not exceed
X. If X == 1, then just write the header on the file “Team StudentName”
and if X == 0, then do not write anything to the file. There will not be more
than one student with the same average. Each of these students will be a
separate line in the new file in the format of “Y) Student Name”, Y being a
number in a list in increasing order, going from 1 - the maximum number of
people per team. The top student will be 1, and then it will go down in
decreasing top scores. The last line of the file should not have a “\n”.
This function will return None unless there is an error.
"""
def form_groups(filename, current_student, num):
    try:
        place = 0
        f1 = open(filename, "r")
        data = f1.readlines()
        f1.close()
        f2 = open("group.txt", "w")
        if num == 0:
            pass
        if num > 1:
            f2.write("Team {}\n".format(current_student))
        if num == 1:
            f2.write("Team {}".format(current_student))
        newlist = []
        newdict = {}
        scores = []
        f1 = open(filename,"r")
        data = f1.readlines()
        for i in data:
            i = i.strip()
            if "," in i:
                newtup = ()
                end = i.find(",")
                first = i[:end]
                last = i[end+2:]
                name = first + " " + last
                newlist.append(name)
        for i in newlist:
            scores.append(get_average(filename, i))
        sortscores = sorted(scores,key=lambda x: x[1], reverse=True)
        for x in sortscores:
            name,score = x
            if place < num and name != current_student and num != 0 and num!= 1:
                if place == num-2 or place == len(sortscores):
                    f2.write(name)
                    place +=1
                    break
                else:
                    f2.write(name + "\n")
                    place +=1
        
            
            
        f2.close()
    except FileNotFoundError:
        return "File is not found."
        
    
#form_groups("students_tester.txt","Shawn Mendes", 1)

"""
Function name: zero_calorie_diet
Parameters: filename (string)
Returns: A string representing the name of a dish
Description: Read in a file of any name but in the format as what is stated
above. If the file is not found, catch a FileNotFoundError and return
“File is not found.”. You are trying to go on a low calorie diet, so parse
through the file and return the name of the dish with the least amount of
calories. If two dishes have the same amount of calories, return the one that
occurred first. 
"""
def zero_calorie_diet(filename):
    try:
        f1 = open(filename, "r")
        head = f1.readline()
        data = f1.readlines()
        f1.close()
        maximum = 100000000
        for i in data:
            i = i.split(",")
            if int(i[2]) < maximum:
                dish = i[0]
                minimum = int(i[2])
        return(dish)
    except FileNotFoundError:
        return "File is not found."
#dish = zero_calorie_diet("menu.csv")         


"""
Function name: erica_menu
Parameters: filename (string), num_of_dishes (int)
Returns: None
Description:  Read in a file of any name but in the format as what is stated
above. If the file is not found, catch a FileNotFoundError and return
“File is not found.”. Erica wants to put together an ideal menu for her,
consisting of the same or less number of items than the number passed in,
but never more. There are conditions, however, since she is broke and very
picky. Parse through the file and create a menu for Erica by choosing the
cheapest dishes. However, never put a Vegetarian dish on her menu, because
she will not eat it. What this means is that if there are 4 dishes on the
list, one being Vegetarian, and she wants 4 items on her menu, then her menu
will consist of 3 dishes. You will be writing this menu out onto a new file
named EricaMenu.txt. The first line of the file will be “Erica’s Menu” and
every corresponding line after that will be the Dish Name, Price, and Cuisine
Type all on the same line, with each dish being on a separate line.
Price will have a $ preceding the number and each element for a line, except
the last element, will be followed by a “, “ (comma and space). The last
line will not have a “\n”. This function will return None, unless there is an
error. 
"""
def erica_menu(filename, num):
    try:
        pricetup = ()
        total = []
        newlist = []
        f1 = open(filename, "r")
        head = f1.readline()
        data = f1.readlines()
        f1.close()
        f2 = open("EricaMenu.txt","w")
        if num==0:
            f2.write("Erica's Menu")
        else:
            f2.write("Erica's Menu\n")
        
        for i in data:
            i = i.split(",")
            food = i[0].strip()
            price = float(i[1][1:].strip())
            nation = i[3].strip()
            if "vegetarian" != nation.lower():
                pricetup = food,price,nation
                total.append(pricetup)
        sorttup = sorted(total,key=lambda x: x[1])
        for x in range(num):
            try:
                newlist.append(sorttup[x])
            except IndexError:
                pass
        for menu in newlist:
            f2.write("{}, ${}, {}\n".format(menu[0],menu[1],menu[2]))
        
        f2.close()        
    except FileNotFoundError:
        return "File is not found."
#erica_menu("menu_tester.csv", 5) 
