#Question one
# Welcome message
print("Hi there! I'm your seconds calculator ")

# Ask for user input
user_input = input(" how many days are we talking about? ")

# Try to convert input to integer
try:
    days = int(user_input)
    
    # Let's do some math (the long way)
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    # Dramatic pause
    print("Calculating...")
    print("Okay, got it!")

    # Final result
    print("In", days, "day(s), there are", seconds, "seconds.")

except:
    print("Oops! That doesn't look like a number. Try again maybe? ")
