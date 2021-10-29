#Sum the digits in the integer
integer = eval(input("Enter a number between 0 and 1000: "))
unitDigit = integer % 10             # % is used here to extract digit
integer1 = integer // 10             # // is used to remove extracted digit
tensDigit = integer1 % 10
integer2 = integer1 // 10
hundredsDigit = integer2 % 10
sum = unitDigit + tensDigit + hundredsDigit
print("The sum of digits is", sum)