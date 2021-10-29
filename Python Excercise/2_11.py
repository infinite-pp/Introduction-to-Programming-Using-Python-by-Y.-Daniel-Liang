#Financial Application: investment amount
finalAccountValue = eval(input("Enter final account value: "))
interestRate = eval(input("Enter annual interest rate: "))
years = eval(input("Enter number of years: "))
monthlyInterestRate = interestRate / 1200    #1200 = 12 * 100 ///// as 12 months and 100 for percentage
initialDepositAmount = finalAccountValue / ((1 + monthlyInterestRate) ** (years * 12))
print("Initial deposit value is", initialDepositAmount)