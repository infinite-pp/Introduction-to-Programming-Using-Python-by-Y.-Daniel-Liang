#Find the number of years and days
minutes = eval(input("Enter the number of minutes: "))
days = minutes // 1440      # integer division give the no. of days
years = days // 365         
remainingDays = days % 365
print(minutes, "minutes is approximately", years, "years and", remainingDays, "days") 