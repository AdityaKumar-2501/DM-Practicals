import matplotlib.pyplot as plt

class RuleSet:
    def __init__(self, age, agegroup, height, status, yearsmarried):
        self.age = age
        self.agegroup = agegroup
        self.height = height
        self.status = status
        self.yearsmarried = yearsmarried
    
    def checkAge(self):
        if self.age >=0 and self.age<=150 :
            return True
        return False
    
    def checkYearsmarried(self):
        if self.age > self.yearsmarried :
            return True
        return False
    
    def checkStatus(self):
        if self.status == "single" or self.status == "married" or self.status == "widowed":
            return True
        return False
    
    def checkAgeGroup(self):
        if self.age < 18 and self.agegroup == "child":
            return True
        elif self.age >=18 and self.age<=65 and self.agegroup == "adult":
            return True
        elif self.age > 65 and self.agegroup == "elderly":
            return True
        else:
            return False
        
    def checkHeight(self):
        if self.height > 0:
            return True
        return False
    
    def checkRuleSet(self):
        if self.checkAgeGroup() and self.checkAge() and self.checkYearsmarried() and self.checkStatus() and self.checkHeight():
            return True
        return False
    



file = open('people.txt', 'r')
fileLine = []
peopleList = []
for line in file:
    fileLine.append(line)
file.close()

for i in range(1,len(fileLine)):
    temp = fileLine[i].split()
    peopleList.append(RuleSet(int(temp[0]), temp[1], float(temp[2]), temp[3], int(temp[4])))

validData = 0

for i in peopleList:
    if i.checkRuleSet() == True:
        validData += 1

invalidData = len(peopleList) - validData
print("validData : ", validData)
print("Invalid data : ", invalidData)

# options = ['Valid Data', 'Invalid Data']
# value = [validData , invalidData]

# print(value)
# plt.bar(options, value, color="blue", width="0.4")
# plt.ylabel("Number of data")
# plt.show()

Options = ['Valid Data' ,  'Invalid Data']
Value = [validData ,invalidData]

plt.bar(Options, Value, color ='red',
        width = 0.6)
plt.ylabel('No. of Data')
plt.show()