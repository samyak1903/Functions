#Q.1- Create a function to calculate the area of a sphere by taking radius from user.
def area(radius):
    return (4*3.14*(radius**2))
rad=float(input("Enter the radius of sphere"))
area=area(rad)
print("Area of sphere= ",round(area,2))
