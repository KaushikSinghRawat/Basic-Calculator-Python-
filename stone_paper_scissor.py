# Stone/Paper/Scissor Player with a Score Counter

import random

stone_paper_scissor = None
score = 0

while stone_paper_scissor != 'quit':
    stone_paper_scissor = input("Stone, Paper or Scissor (Type Quit or Score): ").strip().lower()
    
    random_num_generator = random.randrange(0, 3) #Stone = 0, Paper = 1, Scissor = 2
    rand_list = ("stone", "paper", "scissor")
    
    if stone_paper_scissor == "score":
        print (f"Score : {score}")

    elif stone_paper_scissor == rand_list[random_num_generator]:
        print (f"{rand_list[random_num_generator].capitalize()}!")
        print ("Draw")

    else:
        if stone_paper_scissor == "stone":
            if rand_list[random_num_generator] == "paper":
                print (f"{rand_list[random_num_generator].capitalize()}!")
                print ("Lost!")
            else:
                score += 1
                print (f"{rand_list[random_num_generator].capitalize()}!")
                print ("Victory!")
        
        elif stone_paper_scissor == "paper":
            if rand_list[random_num_generator] == "scissor":
                print (f"{rand_list[random_num_generator].capitalize()}!")
                print ("Lost!")
            else:
                score += 1
                print (f"{rand_list[random_num_generator].capitalize()}!")
                print ("Victory!")

        elif stone_paper_scissor == "scissor":
            if rand_list[random_num_generator] == "stone":
                print (f"{rand_list[random_num_generator].capitalize()}!")
                print ("Lost!")
            else:
                score += 1
                print (f"{rand_list[random_num_generator].capitalize()}!")
                print ("Victory!")





