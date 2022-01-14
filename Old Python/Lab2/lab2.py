#Elijah Peterson
# I worked on this assignment alone using only this semester's materials

import matplotlib.pyplot as plt
import json


def monthfires(filename):
    total = 0
    newlist = []
    hot = {}
    newdict = {}
    f1 = open(filename)
    header = f1.readline()
    data = f1.readlines()
    for i in data:
        i = i.split(",")
        month = i[2]
        newlist.append(month)

    out = [0] * len(newlist)
    
    for x in newlist:
        if x not in newdict:
            newdict[x] = 0
        else:
            newdict[x] += 1

    for keys in newdict:
        total += newdict[keys]

    for keys in newdict:
        perc = newdict[keys] / total
        if perc > .25:
            hot[keys] = newdict[keys]
    
    plt.bar(range(len(hot)), hot.values(), align = "center")
    plt.xticks(range(len(hot)), list(hot.keys()))
    plt.title("Amount of Fires in Months with 25% or More of the Total Fires")
    plt.show()
    return (hot)
    
print(monthfires("forestfires.csv"))

def daysfires(filename):
    newlist = []
    tuplist = []
    newdict = {}
    f1 = open(filename)
    header = f1.readline()
    data = f1.readlines()
    for i in data:
        i = i.split(",")
        days = i[3]
        newlist.append(days)

    for i in newlist:
        if i not in newdict:
            newdict[i] = 0
        else:
            newdict[i] += 1
    
    for i in newdict:
        newtup = ()
        newtup += (newdict[i],i)
        tuplist.append(newtup)
        tuplist.sort(reverse = True)

    mostval,mostday = tuplist[0]
    
    plt.bar(range(len(newdict)), newdict.values(), align = "center")
    plt.xticks(range(len(newdict)), list(newdict.keys()))
    plt.title("Frequency of Forest Fires by Day")
    plt.show()
    return (mostday)
        

print(daysfires("forestfires.csv"))

def isifires(filename):
    tuplist = []
    newdict = {}
    isilist = []
    
    f1 = open(filename)
    header = f1.readline()
    data = f1.readlines()
    for i in data:
        newtup = ()
        i = i.split(",")
        ffmc = i[4]
        isi = i[7]
        isilist.append(float(isi))
        newtup = ffmc,isi
        if newtup not in tuplist:
            tuplist.append(newtup)
    tuplist.sort(reverse = True)
    tuplist = tuplist[0:6]

    isilist.sort(reverse = True)
    for x,y in tuplist:
        plt.scatter(x,y)
    plt.title("FFMC vs ISI")
    plt.show()
        
    maximum = isilist[0]
    if float(tuplist[0][1]) > maximum:
        return True
    else:
        return False
    
   
print(isifires("forestfires.csv"))

def irislen(filename):
    newdict = {}
    newlist = []
    myfile = open(filename,"r")
    json_string = myfile.read()
    mydict = json.loads(json_string)
    myfile.close()
    setosa = 0
    versi = 0
    virginica = 0
    for i in range(0,150):
        types = mydict["data"][i]["class of iris: setosa/versicolor/virginica"]
        petallen = mydict["data"][i]["petal_length in cm"]
        if types == "Iris-setosa":
            setosa += petallen
            averageset = setosa/50
        if types =="Iris-versicolor":
            versi += petallen
            averageversi = versi/50
        if types =="Iris-virginica":
            virginica += petallen
            averagevirgin = virginica/50
    
    newdict["Iris-setosa"] = averageset
    newdict["Iris-versicolor"] = averageversi
    newdict["Iris-virginica"] = averagevirgin
    for i in newdict:
        newtup = ()
        newtup += i,newdict[i]
        newlist.append(newtup)
    newlist.sort(reverse = True)
    maximum = newlist[0][0]
    
    plt.bar(range(len(newdict)), newdict.values(), align = "center")
    plt.xticks(range(len(newdict)), list(newdict.keys()))
    plt.title("Average Petal Length")
    plt.show()
    return(maximum)
print(irislen("iris.json"))

def iriswid(filename):
    newdict = {}
    newlist = []
    myfile = open(filename,"r")
    json_string = myfile.read()
    mydict = json.loads(json_string)
    myfile.close()
    setosa = 0
    versi = 0
    virginica = 0
    for i in range(0,150):
        types = mydict["data"][i]["class of iris: setosa/versicolor/virginica"]
        petalwid = mydict["data"][i]["petal_width in cm"]
        if types == "Iris-setosa":
            setosa += petalwid
            averageset = setosa/50
        if types =="Iris-versicolor":
            versi += petalwid
            averageversi = versi/50
        if types =="Iris-virginica":
            virginica += petalwid
            averagevirgin = virginica/50
    
    newdict["Iris-setosa"] = averageset
    newdict["Iris-versicolor"] = averageversi
    newdict["Iris-virginica"] = averagevirgin
    for i in newdict:
        newtup = ()
        newtup += i,newdict[i]
        newlist.append(newtup)
    newlist.sort(reverse = True)
    maximum = newlist[0][0]
    
    plt.bar(range(len(newdict)), newdict.values(), align = "center")
    plt.xticks(range(len(newdict)), list(newdict.keys()))
    plt.title("Average Petal Width")
    plt.show()
    return(maximum)
print(iriswid("iris.json"))


def irissep(filename):
    newdict = {}
    newlist = []
    myfile = open(filename,"r")
    json_string = myfile.read()
    mydict = json.loads(json_string)
    myfile.close()
    setosa = 0
    versi = 0
    virginica = 0
    for i in range(0,150):
        types = mydict["data"][i]["class of iris: setosa/versicolor/virginica"]
        seplen = mydict["data"][i]["sepal_length in cm"]
        if types == "Iris-setosa":
            setosa += seplen
            averageset = setosa/50
        if types =="Iris-versicolor":
            versi += seplen
            averageversi = versi/50
        if types =="Iris-virginica":
            virginica += seplen
            averagevirgin = virginica/50
    
    newdict["Iris-setosa"] = averageset
    newdict["Iris-versicolor"] = averageversi
    newdict["Iris-virginica"] = averagevirgin
    for i in newdict:
        newtup = ()
        newtup += i,newdict[i]
        newlist.append(newtup)
    newlist.sort(reverse = True)
    maximum = newlist[0][0]
    
    plt.bar(range(len(newdict)), newdict.values(), align = "center")
    plt.xticks(range(len(newdict)), list(newdict.keys()))
    plt.title("Average Sepal Length")
    plt.show()
    return(maximum)
print(irissep("iris.json"))


