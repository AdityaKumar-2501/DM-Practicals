import copy
import matplotlib.pyplot as plt


class iris:
    def __init__(self, sepalLength,sepalWidth,petalLength,petalWidth,species):
        self.sepalLength = sepalLength
        self.sepalWidth = sepalWidth
        self.petalLength = petalLength
        self.petalWidth = petalWidth
        self.species = species

    def value(self):
        val = self.sepalLength+','+self.sepalWidth+','+self.petalLength+','+self.petalWidth+','+self.species
        return val

    def constraint(self):
        res = [0,0,0,0,0]  # 0 means false(no constraint voilated) and 1 means true
        speciesValue  = ['"setosa"\n' , '"versicolor"\n','"virginica"\n']
        if self.species not in speciesValue:
            res[0] = 1  # contraint voialated
        else : res[0] = 0 #
        
        if (self.sepalLength == 'NA' or self.sepalWidth == 'NA' or self.petalLength == 'NA' or self.petalWidth == 'NA'):
            return res
        
        if (float(self.sepalLength) < 0 or float(self.sepalWidth) < 0 or float(self.petalLength) < 0 or float(self.petalWidth) < 0):
            res[1] = 1
        if (float(self.petalLength) < 2*float(self.petalWidth)):
            res[2] = 1
        if (float(self.sepalLength) > 30.0):
            res[3] = 1
        if (float(self.sepalLength) < float(self.petalLength) or float(self.sepalWidth) < float(self.petalWidth)):
            res[4] = 1

        
        return res

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

for l in range(0, len(irisList)):
    try:
        if (float(irisList[l].sepalLength) <= 0.000 or irisList[l].sepalLength == 'Inf'):
            irisList[l].sepalLength = "NA"
        if (float(irisList[l].sepalWidth) <= 0.0000 or irisList[l].sepalWidth == 'Inf'):
            irisList[l].sepalWidth = "NA"
        if (float(irisList[l].petalLength) <= 0.0000 or irisList[l].petalLength == 'Inf'):
            irisList[l].petalLength = "NA"
        if (float(irisList[l].petalWidth) <= 0.0000 or irisList[l].petalWidth == 'Inf'):
            irisList[l].petalWidth = "NA"
    except:
        continue

fileWrite = open("dirty_iris.csv", "w")

for l in range(0, len(irisList)):
    fileWrite.write(irisList[l].value())

fileWrite.close()

# ii is completed

# iii started

ruleVoilated = [0,0,0,0,0]

for i in range(1 , len(irisList)):
    result = originalirisList[i].constraint()
    for j in range(0 , 5):
        ruleVoilated[j] += result[j]  # adds how many time ruleVoilated by checing columnwise
    
print("Species Rule Voilated : " , ruleVoilated[0])
print("Postive value Rule Voilated : " , ruleVoilated[1])
print("Petal Length Rule Voilated : " , ruleVoilated[2])
print("Sepal length Rule Voilated : " , ruleVoilated[3])
print("Sepal longer than its Petals Rule Voilated : " , ruleVoilated[4])

# iii completed 

# iv and v starts

Options = ['Species Rule Voilated', 'Postive Value Rule Voilated', 'Petal Length Rule Voilated', 'Sepal Length Rule Voilated', 'Sepal Longer than its Petals Rule Voilated']

plt.bar(Options, ruleVoilated, color='red', width= 0.6)
plt.ylabel('Number of Rule Voilated')
plt.title('Total Data : ' + str((len(irisList) -1))) # -1 beacuse 1st row is header row

plt.show()

seplaLengthList = []

for i in range(1, len(irisList)):
    try:
        seplaLengthList.append(float(irisList[i].sepalLength))
    except:
        continue
    
graph = plt.boxplot(seplaLengthList)
plt.title("Sepal length")
plt.show()
print (graph)