name = input ("Hello, I am Python. What is your name? ")
print ("Hello "+name)

a = int(input ("Please enter the first leg: "))
b = int(input ("Please enter the second leg "))
c = int(input ("Please enter the third leg: "))

if int(c > a + b):
    print("This is not a triangle.")
if int(c == ((a**2)+(b**2))**(1/2)):
    print("This is a right triangle.")
if int(c > ((a**2)+(b**2))**(1/2)):
    print ("This triangle is obtuse.")
if int(c < ((a**2)+(b**2))**(1/2)):
    print ("This triangle is acute.")