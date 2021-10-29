#Financial application: calculate tips
subtotal, gratuityRate = eval(input("Enter the subtotal and a gratuity rate: "))
gratuity = subtotal * (gratuityRate * 0.01)
total  = subtotal + gratuity
print("The gratuity is", int(gratuity*100)/100, "and the total is", int(total*100)/100)