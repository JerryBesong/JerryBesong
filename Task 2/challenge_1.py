import math

print("Hello There? ") 
print("Do you mind use doing some math? ")
print("i will be needing you to give me three sides of a triangle")
side1 = int(input("side one? " ))
side2 = int(input("side two? " ))
side3 = int(input("side three? " ))
print(side1,side2,side3)

s =(side1 + side2 + side3)/2
print(s)

area = (s*(s-side1)*(s-side2)*(s-side3))
print(area)

square_area = math.sqrt(area)
print(square_area)

print("THANK YOU")