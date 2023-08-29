import random
import math

# Grabs input
minimum = int(input("Enter a minimum number: "))

# Grabs input
maximum = int(input("Enter a maximum number: "))

# Generates random number between minimum and maximum number
x = random.randint(minimum, maximum)
print("\n You only have ", round(math.log(maximum - minimum + 1, 2)), "chances remaining to guess the number.\n")

# Initializes the number of guesses starting at 0
count = 0

while count < math.log(maximum - minimum + 1, 2):
    count += 1
    
    # Grabs guess number input
    guess = int(input("Guess a number: "))
    
    # Tests to see if number was guessed correctly
    if x == guess:
        print("Congrats! You guessed correctly in ", count, "tries.")
        
        # Loop breaks if number is guessed correctly
        break
    elif x > guess:
        print("Wrong - try again. Guess a higher number.")
    elif x < guess:
        print("Wrong - try again. Guess a lower number.")
    
# If guess attempts are exceeded, shows number.     
if count >= math.log(maximum - minimum + 1, 2):
    print("\n The number was %d" % x)