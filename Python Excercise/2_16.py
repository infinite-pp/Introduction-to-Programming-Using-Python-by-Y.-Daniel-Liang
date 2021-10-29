#Physics: Acceleration 

v0, v1, t = eval(input("Enter v0, v1, and t: "))
acceleration = (v1 - v0) / t

print("The average acceleration is", (round(acceleration * 10000) / 10000))