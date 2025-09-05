def check_case(ch):
    """Function to determine if a character is uppercase or lowercase"""
    if ch.isupper():
        return "uppercase"
    elif ch.islower():
        return "lowercase"
    else:
        return "not a letter"

def main():
    # Ask the user to enter a character
    char = input("Enter a single character: ")

    # Ensure only one character is entered
    if len(char) != 1:
        print("Please enter only one character.")
    else:
        result = check_case(char)
        print(f"The character '{char}' is {result}.")

# Run the program
main()
