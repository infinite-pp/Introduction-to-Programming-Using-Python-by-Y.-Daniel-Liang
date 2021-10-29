#Financial application: Calculate future investment value
investAmount = eval(input("Enter investment amount: "))
annualInterestRate = eval(input("Enter annual interest rate: "))
numberOfYears = eval(input("Enter number if years: "))

monthlyInterestRate = annualInterestRate / 1200
numberOfMonths = numberOfYears * 12

futureInvestmentValue = investAmount * (1 + monthlyInterestRate) ** numberOfMonths

print("Accumulated value is", (int(futureInvestmentValue * 100) / 100))