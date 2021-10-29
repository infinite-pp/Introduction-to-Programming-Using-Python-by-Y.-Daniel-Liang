#Physics: Find runway length
speed, acceleration = eval(input("Enter speed and acceleration: "))
length = (speed * speed) / (2 * acceleration) 
#print("The minimum runway length gor this airplane is", str(round(length * 1000) / 1000), "meters")
print("The minimum runway length gor this airplane is", (round(length * 1000)) / 1000, "meters")