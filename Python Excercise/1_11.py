birthInDay = 24 * 60 * 60 / 7
deathInDay = 24 * 60 * 60 / 13
immigrantInDay = 24 * 60 * 60 / 45
populationIncreasePerDay = birthInDay + immigrantInDay - deathInDay
populationIncreasePerYear = populationIncreasePerDay * 365
presentPopulation = 312032486
firstYearPopulation = presentPopulation + populationIncreasePerYear
secondYearPopulation = firstYearPopulation + populationIncreasePerYear
thirdYearPopulation = secondYearPopulation + populationIncreasePerYear
forthYearPopulation = thirdYearPopulation + populationIncreasePerYear
fifthYearPopulation = forthYearPopulation + populationIncreasePerYear
print(firstYearPopulation, secondYearPopulation, thirdYearPopulation, forthYearPopulation, fifthYearPopulation)