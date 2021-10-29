#Compute the volume and area of a cylinder
PI = 3.14159
#Take user input seperated by comma
radius, length = eval(input("Enter the radius and length of a cylinder: "))
volume = PI * radius * radius * length
area = 2 * PI * radius * length
print("The volume is", volume)
print("The area is", area)
