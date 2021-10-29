#Calculate Energy
mass = eval(input("Enter the amount of water in kilogram: "))
initialTemp = eval(input("Enter the initial temperature: "))
finalTemp = eval(input("Enter the final temperature: "))
energyNeeded = mass * (finalTemp - initialTemp) * 4184
print("The energy needed is", energyNeeded)