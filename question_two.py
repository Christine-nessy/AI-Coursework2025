import math

def sphere_volume():
    # Get radius from the user
    r = float(input("Please enter the radius of the sphere: "))

    # Compute volume with exponent operator
    volume = (4/3) * math.pi * (r ** 3)

    # Output result with better formatting
    print("The volume of a sphere with radius", r, "is:", round(volume, 3))

# Run the function
sphere_volume()



