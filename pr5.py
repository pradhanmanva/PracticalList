#WAP to find the roots of the quadratic equation

a = 1
b = -4
c = 4

D = (b**2 - (4*a*c))**(1/2)

if (D < 0):
    print("The roots are imaginary.")
elif (D == 0):
    x =  ((-1)*b)/(2*a)
    print("The root are equal. x= "+str(x))
else :
    x1 = (((-1)*b)+D)/(2*a)
    x2 = (((-1) * b) - D) / (2 * a)
    print("The roots are x1 = "+str(x1)+" and x2 = "+str(x2))