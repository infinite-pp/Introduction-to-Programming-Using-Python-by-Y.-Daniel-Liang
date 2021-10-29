#Split digits
integer = eval(input("Enter a four-digit integer: "))
unitDigit = integer % 10
integer1 = integer // 10
tensDigit = integer1 % 10
integer2 = integer1 // 10
hundredsDigit = integer2 % 10
integer3 = integer2 // 10
thoudandsDigit = integer3 % 10
print(unitDigit)
print(tensDigit)
print(hundredsDigit)
print(thoudandsDigit)