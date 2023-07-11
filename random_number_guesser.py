#Random Number Guesser which generates a random number and requests a answer.
#If the answer is not correct, displays whether the answer is lower or higher from the random number

import random

top_range = int(input("Enter the top range: ").strip())
bottom_range = int(input("Enter the bottom range: ").strip())

rand_generator = random.randrange(bottom_range, top_range + 1)

checker = False

while checker == False:
    answer = int(input("Enter your guess: ").strip())

    if rand_generator == answer:
        print (f"Correct, the Random Number was {rand_generator}")
        checker = True
    else:
        if rand_generator < answer:
            print ("The random number is lower")
        else: 
            print ("The random number is higher")

