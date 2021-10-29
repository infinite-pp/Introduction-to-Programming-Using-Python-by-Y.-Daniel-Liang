#Financial Application: compound value
monthlySavingAmount = eval(input("Enter the monthly saving amount: "))
annualInterestRate = eval(input("Enter a value for annual interest rate: "))
monthlyInterstRate = annualInterestRate / 1200
amount1 = monthlySavingAmount * (1 + monthlyInterstRate)
amount2 = (monthlySavingAmount + amount1) * (1 + monthlyInterstRate)
amount3 = (monthlySavingAmount + amount2) * (1 + monthlyInterstRate)
amount4 = (monthlySavingAmount + amount3) * (1 + monthlyInterstRate)
amount5 = (monthlySavingAmount + amount4) * (1 + monthlyInterstRate)
amount6 = (monthlySavingAmount + amount5) * (1 + monthlyInterstRate)

print("After the sixth month, the account value is", (round(amount6 * 100) / 100))