def main():
    numbers = []  # Empty list (array) to hold the values

    print("Enter 5 numbers:")

    # Loop to take 5 inputs
    for i in range(5):
        value = float(input(f"Enter value {i+1}: "))
        numbers.append(value)

    # Calculate average
    average = sum(numbers) / len(numbers)

    # Display the result
    print("\nThe numbers you entered are:", numbers)
    print("The average is:", average)

# Run the program
main()
