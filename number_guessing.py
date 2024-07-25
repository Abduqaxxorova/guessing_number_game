from random import randint
from math import log2

print("Hello! Are you ready play a game with me:)")

lower_bound = int(input("Please write lower bound:"))
upper_bound = int(input("Please write upper bound:"))

count = 0
red = False

number = randint(lower_bound, upper_bound)
total_chances = log2(upper_bound-lower_bound+1)

while count <= total_chances:
    count +=1

    guess = int(input("Please guess a number!"))

    if guess == number:
        print("Congratulations! You've guessed the number correctly.")
        red = True
        break
    elif guess < number:
        print("Try again! It is too low:(")
    else:
        print("Try again! It is too high:(")

if not red:
    print(f"Sorry, you've run out of chances. The number was {number}.")