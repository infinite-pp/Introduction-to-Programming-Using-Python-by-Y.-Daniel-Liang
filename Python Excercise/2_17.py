#Health application: Compute BMI
pounds = eval(input("Enter weight in pouds: "))
height = eval(input("Enter height in inches: "))
kilograms = 0.45359237 * pounds
meters = 0.0254 * height
BMI = kilograms / meters ** 2
print("BMI is", (round(BMI * 10000) / 10000))