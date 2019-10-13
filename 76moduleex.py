pi = 3.14159

def area(radius):
    return 4 * pi * (radius * radius)

def volume (radius):
    return (4.0/3.0) * pi * (radius * radius * radius)  

print("Enter the radiusof the sphere: ") 
radius = int(input())
print("The area is " + str(area(radius))) 
print("The volume is " + str(volume(radius))) 
   