import copy

class iris:
    def __init__(self, sepalLength,sepalWidth,petalLength,petalWidth,species):
        self.sepalLength = sepalLength
        self.sepalWidth = sepalWidth
        self.petalLength = petalLength
        self.petalWidth = petalWidth
        self.species = species


irisList = []
fileLine = []
file = open('dirty_iris.csv', 'r')
for i in file:
    fileLine.append(i)

file.close()

for i in range(1, len(fileLine)):
    temp = fileLine[i].split(',')
    irisList.append(iris(temp[0], temp[1],temp[2], temp[3], temp[4]))

originalirisList = copy.deepcopy(irisList) # storing the original list which can't be change by ching in irisList
irisdataLength = len(irisList) -1 #as first row is heading in data set

incompleteData = 0;

for i in irisList:
    if i.sepalLength == "NA" or i.sepalWidth == "NA" or i.petalLength == "NA" or i.petalWidth == "NA" or i.species == "NA":
        incompleteData += 1

print("Total DATA : " , irisdataLength)
print("Total Incomplete Data : " , incompleteData)
print("********************************")
print("Percentage of Incomplete Data : " , round((incompleteData/irisdataLength)*100 , 2) , " %")

# i part completed 

# ii  part starting 
