mport random

# Generate a random signed number
number = random.randint(-10, 10)

# Check if the number is positive, negative, or zero
if number > 0:
        print(number, "is positive")
    elif number == 0:
            print(number, "is zero")
        else:
                print(number, "is negative")

