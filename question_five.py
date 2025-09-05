def main():
    # Initialize variables
    x = 0
    y = 20

    # Repeat until y < 6
    while y >= 6:
        y = y - 4        # Subtract 4 from y
        x = x + (2 / y)  # Add 2/y to x

    # Display result
    print("Final value of x:", x)

# Run the program
main()
