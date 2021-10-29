#Financial Applicatio: Calculate Interest
balance, annualInterestRate = eval(input("Enter balance and interest rate (e.g., 3 for 3%): "))
interest = balance * (annualInterestRate / 1200)
print("The interst on the next monthly payment is", (round(interest * 100000) / 100000))