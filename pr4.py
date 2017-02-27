# WAP to calculate the area of the triangle

side1 = 10
side2 = 6
side3 = 8
semi = (side1 + side2 + side3) / 2

area = (semi * (semi - side1) * (semi - side2) * (semi - side1)) ** (1 / 2)
print("Area of the triangle with sides "+str(side1)+", "+str(side2)+" and "+str(side3)+" : "+str(area)+". ")

