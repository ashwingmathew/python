import random
number = random.randrange(1,9)
guess = int(input("Guess a number between 1 and 9: "))
if guess < number:
    print("Too low")
elif guess > number:
    print("Too high")
elif guess == number:
    print("You've guessed it right!")               
