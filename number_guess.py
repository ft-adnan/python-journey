# Number Guessing Game 🎯
import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("🎉 You guessed it right!")
else:
    print(f"Oops! The number was {number}. Try again!")

print("Thanks for playing!")
