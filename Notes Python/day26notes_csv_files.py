# Day 26 - writing to files and introducing csv data files

# download the file crime_data.csv from Canvas>files>lecture notes>lecture files

newf = open("myfile.txt","w") # creates the file if it doesn't exist
                        # overwrites the file if it already exists

newf.write("Hello\n")
newf.write("Goodbye\n")
newf.close()      # nothing is written until the file is closed!


# copy lines 0,2,and 4 to newpoem
f1 = open("poem.txt","r")
f2 = open("newpoem.txt","w")
lines = f1.readlines()
for num in range(0,len(lines),2):
    f2.write(lines[num])
f1.close()
f2.close()

# create a new file called newpoem.txt that is poem.txt without any e's
f1 = open("poem.txt","r")
f2 = open("newpoem.txt","w")
poem = f1.read()
poem = poem.replace("e","")
f2.write(poem)
f1.close()
f2.close()


# open the file gtsong.txt and change the word "hell" to "heck" save the
# new file as clean_gtsong.txt
f1 = open("gtsong.txt","r")
f2 = open("clean_gtsong.txt","w")
poem = f1.read()
poem = poem.replace("hell","heck")
f2.write(poem)
f1.close()
f2.close()


# csv stands for comma separated values
# csv files almost always have the first line as the headings
# commas separate the data into columnns


# how many crimes happened in the year 2015?
f = open("crime_data.csv","r")
headings = f.readline()   # keep the first line separate
datalines = f.readlines() # now read all the other lines
count = 0
for line in datalines:
    pieces = line.split(",")
    #print(pieces[7])
    
    if pieces[7][-2:] == "15"   :  # all file data is strings
        count += 1
    
print(count)
f.close()






