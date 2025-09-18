print("This is a program use to calculate the area of a cone")
radius = float(input("Enter the radius of the base\n"))
slant_height = float(input("Please enter the Slant height of the cone\n"))
pI = 3.14
area = pI*radius*radius + pI*radius*slant_height
print("The area of the cone is: ", area)