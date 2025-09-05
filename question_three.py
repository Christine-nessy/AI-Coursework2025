def compute_area(side):
    """Function to compute the area of a square"""
    return side ** 2

def compute_perimeter(side):
    """Function to compute the perimeter of a square"""
    return 4 * side

def main():
    # Ask the user for the side length
    side = float(input("Enter the side length of the square: "))

    # Calculate area and perimeter
    area = compute_area(side)
    perimeter = compute_perimeter(side)

    # Display the results
    print(f"\nFor a square with side {side}:")
    print(f"Area = {area}")
    print(f"Perimeter = {perimeter}")

# Run the program
main()
