#Population Projection
numberOfYears = eval(input("Enter the number of years: "))

birthInDay = 24 * 60 * 60 / 7
deathInDay = 24 * 60 * 60 / 13
immigrantInDay = 24 * 60 * 60 / 45
populationIncreasePerDay = birthInDay + immigrantInDay - deathInDay
populationIncreasePerYear = populationIncreasePerDay * 365
presentPopulation = 312032486

population = presentPopulation + numberOfYears * populationIncreasePerYear

print("The population is", (round(population)))