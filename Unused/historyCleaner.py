#############################################################
#   BE CAREFUL WITH THIS SCRIPT!
#   IT DELETES FILES! MAKE SURE YOUR DIRECTORY IS FULL PATH!
#############################################################


#Deletes empty history files.
#Lists duplicates for further review

import os
import re

directory = input("Enter target directory: ")
filenum = 0
deleteNum = 0

for filename in os.scandir(directory):
    if filename.is_file():
        filenum += 1
        print(str(filenum) + ": Found: " + filename.name)
        file = open(filename, "r")
        filecontents = file.read()
        if not(re.search('[a-zA-Z]', filecontents)):
            print(filename.name + " contains nothing! Deleting...")
            path = os.path.join(directory, filename.name)
            file.close()
            os.remove(path)
            deleteNum += 1
            print(filename.name + " removed.")
        else:
            file.close()
dirSize = 0
for filename in os.scandir(directory):
    dirSize += 1
    
print("All empty files deleted: " + str(deleteNum) + "/" + str(filenum) + " deleted.")
print(str(dirSize) + " files remaining. Attempting duplicate check...")

previousNumber = ""
previousFile = ""
duplicatesNum = 0

for filename in os.scandir(directory):
    currentFile = filename.name
    currentNumber = currentFile.split("-")[0]
    if currentNumber == previousNumber:
        print("Duplicates detected! " + previousFile + " and " + currentFile)
        duplicatesNum += 2
    previousFile = filename.name
    previousNumber = previousFile.split("-")[0]
print(str(duplicatesNum) + " duplicate files found.")