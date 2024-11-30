age = int(input("Enter your age:"))
gender = input("Enter your gender m/w or M/N")
trainType= int(input("enter train type: 1-3"))

isMale = True if gender == "m" or "M" else False
minVals, maxVals = [0,0.50,0.7,0.8], [0,0.7,0.8,0.87]
maxPulse = (220- age) if isMale else (206-0.88*age)
resString = str(int(((maxPulse*minVals[trainType])))) + " kuni " + str(int((maxPulse*maxVals[trainType])))
print(resString)
