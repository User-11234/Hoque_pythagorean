name = input ("Hello, I am Python. What is your name? ")

print ("Hello "+name)

a = float(input ("Please enter the first leg of the triangle: "))
b = float(input ("Please enter the second leg of the triangle: "))

c = (((a**2)+(b**2))**(1/2))

print ("According to the Pythogorean theorem, the last leg of your triangle would be "+str(c)+".")